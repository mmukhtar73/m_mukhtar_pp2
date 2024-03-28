
import pygame

pygame.init()

w, h = 500, 500
screen = pygame.display.set_mode((w, h))

c_x, c_y, r, move = w/2, h/2, 25, 20

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and c_y >= r:
                c_y -= move
            if event.key == pygame.K_DOWN and c_y <= h - r:
                c_y += move
            if event.key == pygame.K_LEFT and c_x >= r:
                c_x -= move
            if event.key == pygame.K_RIGHT and c_x <= w - r:
                c_x += move

    screen.fill("white")

    pygame.draw.circle(screen, "red", (c_x, c_y), r)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
