
import pygame


def main():
    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'
    points = []

    eraser = False

    pygame.image.save(screen, "screenshot.png")
    pygame.image.save(screen, "screenshot0.png")
    screenshot = pygame.image.load("screenshot.png")

    shape = 'circle'

    while True:
        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            # determine if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # determine if a letter key was pressed
                if event.key == pygame.K_e:
                    points = []
                    eraser = not eraser

                    pygame.image.save(screen, "screenshot.png")
                    screenshot = pygame.image.load("screenshot.png")
                if event.key == pygame.K_d:
                    screenshot = pygame.image.load("screenshot0.jpg")
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_y:
                    mode = 'yellow'
                elif event.key == pygame.K_c:
                    mode = 'cyan'
                elif event.key == pygame.K_m:
                    mode = 'magenta'
                elif event.key == pygame.K_w:
                    mode = 'white'
                elif event.key == pygame.K_s:
                    shape = 'square'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3:  # right click shrinks radius
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]

        screen.blit(screenshot, (0, 0))

        # draw all points
        if not eraser:
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode, shape)
                i += 1
        else:
            i = 0
            while i < len(points) - 1:
                erase(screen, points[i], points[i + 1], radius)
                i += 1

        pygame.display.flip()

        clock.tick(60)


def erase(screen, start, end, width):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, (0, 0, 0), (x, y), width)


def drawLineBetween(screen, index, start, end, width, color_mode, shape='circle'):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'yellow':
        color = (c2, c2, c1)
    elif color_mode == 'cyan':
        color = (c1, c2, c2)
    elif color_mode == 'magenta':
        color = (c2, c1, c2)
    elif color_mode == 'white':
        color = (c2, c2, c2)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        if shape == 'circle':
            pygame.draw.circle(screen, color, (x, y), width)
        elif shape == 'square':
            pygame.draw.rect(screen, color, pygame.Rect(x, y, width * 2, width * 2))


main()
