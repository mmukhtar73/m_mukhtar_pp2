
import math

import pygame


# shape objects to draw
class Object:
    # here radius is width, named radius not to confuse with horizontal length
    def __init__(self, shape, color, start, end, radius):
        self.shape = shape
        self.color = color
        self.start = start
        self.end = end
        self.radius = radius

    # point where we currently hold our cursor, property is used to update greater rect
    @property
    def end(self):
        return self._end

    # includes updating greater rect
    @end.setter
    def end(self, value):
        self._end = value
        self.upd_rect()

    # updates greater rect with change of end (where we hold our cursor)
    def upd_rect(self):
        self.w = abs(self.end[0] - self.start[0])
        self.h = abs(self.end[1] - self.start[1])
        self.adj = (min(self.start[0], self.end[0]), min(self.start[1], self.end[1]))
        self.rect = pygame.Rect(self.adj, (self.w, self.h))

    # makes a smaller rect (a part of greater rect for fixed-proportional shapes)
    def make_mini(self, proportion):
        if self.w == 0: self.w += 1E-10

        if self.h / self.w >= proportion:
            self.side_x = self.w
            self.side_y = self.side_x * proportion
        else:
            self.side_y = self.h
            self.side_x = self.side_y / proportion

        dx = self.side_x if self.end[0] - self.start[0] < 0 else 0
        dy = self.side_y if self.end[1] - self.start[1] < 0 else 0

        self.mini_adj = (self.start[0] - dx, self.start[1] - dy)

        self.mini_rect = pygame.Rect(self.mini_adj, (self.side_x, self.side_y))

    # draw the object depending on shape
    def draw(self, surf):
        if self.shape == "straight":
            pygame.draw.line(surf, self.color, self.start, self.end, self.radius)
        elif self.shape == "rect":
            pygame.draw.rect(surf, self.color, self.rect, self.radius)
        elif self.shape == "square":
            self.make_mini(1)
            pygame.draw.rect(surf, self.color, self.mini_rect, self.radius)
        elif self.shape == "right_tr":
            positions = (
                self.start,
                (self.start[0], self.end[1]),
                (self.end[0], self.start[1])
            )
            pygame.draw.polygon(surf, self.color, positions, self.radius)
        elif self.shape == "equilat":
            self.make_mini(math.sqrt(3) / 2)
            positions = (
                self.mini_rect.bottomleft,
                self.mini_rect.bottomright,
                self.mini_rect.midtop
            )
            pygame.draw.polygon(surf, self.color, positions, self.radius)
        elif self.shape == "rhombus":
            positions = (
                self.rect.midtop,
                self.rect.midleft,
                self.rect.midbottom,
                self.rect.midright
            )
            pygame.draw.polygon(surf, self.color, positions, self.radius)


# text button class for shape change
class Button(pygame.sprite.Sprite):
    def __init__(self, text):
        super().__init__()
        font = pygame.font.SysFont("Verdana", 20)
        self.image = font.render(text, True, "yellow", "gray")
        self.rect = self.image.get_rect()


# here actual program starts
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    # default data about shapes to draw
    radius = 15
    color = "white"
    shape = "straight"
    start = None
    objects = []

    # creating buttons for shape change
    shapes = ["straight", "rect", "square", "rhombus", "right_tr", "equilat", "rhombus"]
    shape_buttons = []

    current_left = 0
    for a_shape in shapes:
        current_button = Button(a_shape)
        current_button.rect.left = current_left
        shape_buttons.append(current_button)
        current_left = current_button.rect.right + 10

    # creating color buttons
    colors = ["red", "yellow", "green", "cyan", "blue", "magenta", "white"]
    color_rects = []

    colors_top = shape_buttons[0].rect.bottom + 10  # makes color buttons lower

    current_left = 0
    for a_color in colors:
        current_rect = pygame.Rect((current_left, colors_top), (20, 20))
        color_rects.append(current_rect)
        current_left = current_rect.right + 10

    # core part of program
    while True:
        screen.fill((0, 0, 0))

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:

                # another way of color change
                if event.key == pygame.K_r:
                    color = "red"
                elif event.key == pygame.K_g:
                    color = "green"
                elif event.key == pygame.K_b:
                    color = "blue"
                elif event.key == pygame.K_y:
                    color = "yellow"
                elif event.key == pygame.K_c:
                    color = "cyan"
                elif event.key == pygame.K_m:
                    color = "magenta"
                elif event.key == pygame.K_w:
                    color = "white"

                # "radius" change
                elif event.key == pygame.K_RIGHT:
                    if radius < 20:
                        radius += 1
                elif event.key == pygame.K_LEFT:
                    if radius > 1:
                        radius -= 1

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                # to not allow creating a new shape if a button is pressed
                button_pressed = False

                # shape buttons press check
                for i in range(len(shapes)):
                    if shape_buttons[i].rect.collidepoint(event.pos):
                        shape = shapes[i]
                        button_pressed = True
                        break

                # color buttons press check
                if not button_pressed:  # if statement is added to not loop if a shape button is pressed
                    for i in range(len(colors)):
                        if color_rects[i].collidepoint(event.pos):
                            color = colors[i]
                            button_pressed = True
                            break

                # create new shape and allow change while we hold a mouse button
                if not button_pressed:
                    start = event.pos
                    objects.append(Object(shape, color, start, end, radius))
            # to detach the shape from cursor
            if event.type == pygame.MOUSEBUTTONUP:
                start = None

        # position of cursor (one of two points to create a shape)
        end = pygame.mouse.get_pos()

        # draw all previous and current shape
        for o in objects:
            o.draw(screen)

        # update current shape state
        if start is not None:
            objects[-1].end = end
            objects[-1].color = color
            objects[-1].radius = radius

        # draw shape buttons above shapes
        for shape_button in shape_buttons:
            screen.blit(shape_button.image, shape_button.rect)

        # draw color buttons above shapes
        for i in range(len(colors)):
            pygame.draw.rect(screen, colors[i], color_rects[i])

        pygame.display.flip()
        clock.tick(60)


main()
