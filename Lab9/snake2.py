
import random
import datetime

import pygame

pygame.init()

# make cells fit the screen
WIDTH = 600
N_COLUMNS, N_ROWS = 20, 20
BS = WIDTH // N_COLUMNS
WIDTH = N_COLUMNS * BS
HEIGHT = N_ROWS * BS

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def from_px(x, y):
        return Point(x // BS, y // BS)
    
    def to_px(self):
        return self.x * BS, self.y * BS
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Snake:
    def __init__(self):
        start_x = WIDTH // 2
        start_y = HEIGHT // 2
        self.body = [
            Point.from_px(start_x, start_y),
            Point.from_px(start_x, start_y),
        ]
        self.tup = [(body_point.x, body_point.y) for body_point in self.body]

    @property
    def size(self):
        return len(self.body)

    def draw(self):
        head = self.body[0]
        Grid.color_cell(RED, head)

        for body_cell in self.body[1:]:
            Grid.color_cell(BLUE, body_cell)

    def move(self, dx, dy):
        last_idx = len(self.body) - 1

        # moving body from tail
        for idx in range(last_idx, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y

        # moving head
        self.body[0].x += dx
        self.body[0].y += dy

        self.tup = [(body_point.x, body_point.y) for body_point in self.body]

    def check_collision(self, food):
        if food.x != self.body[0].x:
            return False
        if food.y != self.body[0].y:
            return False
        return True


class Grid:
    # number of free rows, columns and cells
    n_columns = N_COLUMNS - 2
    n_rows = N_ROWS - 2
    n_cells = n_rows * n_columns

    @staticmethod
    def color_cell(color, point):
        pos = point.to_px()
        cell_rect = pygame.Rect(pos[0], pos[1], BS, BS)
        pygame.draw.rect(SCREEN, color, cell_rect)

    @classmethod
    # background and wall
    def draw_background(cls):
        SCREEN.fill(GRAY)
        field_rect = pygame.Rect(BS, BS, cls.n_columns * BS, cls.n_rows * BS)
        pygame.draw.rect(SCREEN, BLACK, field_rect)

    @staticmethod
    def draw_lines():
        # drawing lines
        for x in range(0, WIDTH, BS):
            pygame.draw.line(SCREEN, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, BS):
            pygame.draw.line(SCREEN, WHITE, (0, y), (WIDTH, y))


class Food:
    def __init__(self, snake):
        location = self.gen_location(snake)
        self.x = location[0]
        self.y = location[1]
        self.weight = random.randint(1, 5)
        self.timer = 20 // self.weight

    @staticmethod
    def gen_location(snake):
        # generating position out of free cells
        n_free = Grid.n_cells - snake.size
        where_to_place = random.randint(0, n_free)

        # loop increments
        free_count = 0
        food_x, food_y = 1, 1
        while free_count < where_to_place:
            # going through columns and rows
            if food_x >= N_COLUMNS - 2:
                food_x = 1
                food_y += 1
            else: food_x += 1
            if food_y >= N_ROWS - 2:
                food_y = 1

            # counting free cells
            if (food_x, food_y) not in snake.tup:
                free_count += 1
        return food_x, food_y

    def draw(self):
        if self.weight == 1:
            Grid.color_cell(GREEN, Point(self.x, self.y))
        elif self.weight == 2:
            Grid.color_cell(YELLOW, Point(self.x, self.y))
        elif self.weight == 3:
            Grid.color_cell(CYAN, Point(self.x, self.y))
        elif self.weight == 4:
            Grid.color_cell(MAGENTA, Point(self.x, self.y))
        elif self.weight == 5:
            Grid.color_cell(WHITE, Point(self.x, self.y))
        else:
            Grid.color_cell(GRAY, Point(self.x, self.y))


def main():
    running = True
    snake = Snake()
    food = Food(snake)

    font = pygame.font.SysFont("Verdana", 30)

    level = 1
    level_surf = font.render(f"Level {level}", True, YELLOW)
    level_rect = level_surf.get_rect()
    
    score = 0
    score_surf = font.render(f"Score: {score}", True, YELLOW)
    score_rect = score_surf.get_rect()
    score_rect.top = level_rect.bottom
    
    dx, dy = 0, 0
    speed = 5
    timestamp = datetime.datetime.now()
    timeout = food.timer
    
    current_difference = (datetime.datetime.now() - timestamp).seconds
    timer_surf = font.render(f"Timer: {current_difference}", True, YELLOW)
    timer_rect = timer_surf.get_rect()
    timer_rect.top = score_rect.bottom

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dy != 1:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN and dy != -1:
                    dx, dy = 0, +1
                elif event.key == pygame.K_RIGHT and dx != -1:
                    dx, dy = 1, 0
                elif event.key == pygame.K_LEFT and dx != 1:
                    dx, dy = -1, 0

        snake.move(dx, dy)

        # collision with wall
        if snake.body[0].x * BS < BS or\
                snake.body[0].y * BS < BS or\
                snake.body[0].x * BS + BS > WIDTH - BS or\
                snake.body[0].y * BS + BS > HEIGHT - BS:
            running = False

        # collision with food
        if snake.check_collision(food):
            snake.body.append(
                Point(snake.body[-1].x, snake.body[-1].y)
            )
            snake.move(dx, dy)
            score += food.weight
            score_surf = font.render(f"Score: {score}", True, YELLOW)
            if score % 5 == 0:
                speed += 5
                level += 1
                level_surf = font.render(f"Level {level}", True, YELLOW)

            # changing location of food
            food = Food(snake)
            timeout = food.timer
            timestamp = datetime.datetime.now()

        # timer
        current_difference = (datetime.datetime.now() - timestamp).seconds
        timer_surf = font.render(f"Timer: {timeout - current_difference}", True, YELLOW)

        # time out of food
        if current_difference >= timeout:
            food = Food(snake)
            timestamp = datetime.datetime.now()

        # collision with body
        starting_state = dx == 0 and dy == 0
        if snake.tup[0] in snake.tup[1:] and not starting_state:
            running = False

        Grid.draw_background()
        snake.draw()
        food.draw()
        Grid.draw_lines()

        SCREEN.blit(level_surf, level_rect)
        SCREEN.blit(score_surf, score_rect)
        SCREEN.blit(timer_surf, timer_rect)

        if running:
            pygame.display.flip()
            clock.tick(speed)


if __name__ == '__main__':
    main()