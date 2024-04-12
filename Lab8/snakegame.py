import pygame
import random

# Init
pygame.init()

# screen
MAP_WIDTH = 600
MAP_HEIGHT = 600
BLOCK_SIZE = 20
FPS = 5  # fps

# Col
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)  
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)  

#  fonts
font = pygame.font.SysFont(None, 25)

#  clock
clock = pygame.time.Clock()

#  display
screen = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))
pygame.display.set_caption("Snake Game")

# snake
def draw_snake(snake):
    for i, segment in enumerate(snake):
        if i == 0:  # Head
            pygame.draw.rect(screen, PURPLE, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
        elif i % 2 == 0:  # pattern
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
        else:
            pygame.draw.rect(screen, DARK_GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

# food
def generate_food(snake):
    while True:
        food_x = random.randint(1, (MAP_WIDTH - BLOCK_SIZE) // BLOCK_SIZE - 1) * BLOCK_SIZE
        food_y = random.randint(1, (MAP_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE - 1) * BLOCK_SIZE
        if (food_x, food_y) not in snake:
            return food_x, food_y

# border
def draw_border():
    pygame.draw.rect(screen, WHITE, (0, 0, MAP_WIDTH, BLOCK_SIZE))
    pygame.draw.rect(screen, WHITE, (0, 0, BLOCK_SIZE, MAP_HEIGHT))
    pygame.draw.rect(screen, WHITE, (0, MAP_HEIGHT - BLOCK_SIZE, MAP_WIDTH - BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, WHITE, (MAP_WIDTH - BLOCK_SIZE, 0, BLOCK_SIZE, MAP_HEIGHT - BLOCK_SIZE))

# loop
def game_loop():
    snake = [(MAP_WIDTH // 2, MAP_HEIGHT // 2)]
    dx = BLOCK_SIZE
    dy = 0
    food_x, food_y = generate_food(snake)
    score = 0
    level = 1
    foods_eaten = 0
    paused = True  # pause

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # start/pause
                    paused = not paused
                elif not paused:
                    if event.key == pygame.K_LEFT and dx == 0:
                        dx = -BLOCK_SIZE
                        dy = 0
                    elif event.key == pygame.K_RIGHT and dx == 0:
                        dx = BLOCK_SIZE
                        dy = 0
                    elif event.key == pygame.K_UP and dy == 0:
                        dy = -BLOCK_SIZE
                        dx = 0
                    elif event.key == pygame.K_DOWN and dy == 0:
                        dy = BLOCK_SIZE
                        dx = 0

        if not paused:
            # Move t
            new_head = (snake[0][0] + dx, snake[0][1] + dy)
            snake.insert(0, new_head)

            
            if (new_head[0] < BLOCK_SIZE or new_head[0] >= MAP_WIDTH - BLOCK_SIZE or
                new_head[1] < BLOCK_SIZE or new_head[1] >= MAP_HEIGHT - BLOCK_SIZE or
                new_head in snake[1:]):
                return score

            # col food
            if new_head == (food_x, food_y):
                food_x, food_y = generate_food(snake)
                score += 1
                foods_eaten += 1
                if foods_eaten == 3:
                    level += 1
                    foods_eaten = 0

            else:
                snake.pop()

        screen.fill(BLUE)
        draw_border()
        draw_snake(snake)
        pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

      
        score_text = font.render(f"Score: {score}", True, BLACK)
        level_text = font.render(f"Level: {level}", True, BLACK)
        screen.blit(score_text, (BLOCK_SIZE, BLOCK_SIZE))
        screen.blit(level_text, (BLOCK_SIZE, BLOCK_SIZE * 2))

        pygame.display.update()
        clock.tick(FPS)

# Start 
final_score = game_loop()
print(f"Final Score: {final_score}")
