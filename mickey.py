
import pygame
import datetime

# initialization
pygame.init()

w_sc, h_sc = 420, 315
screen = pygame.display.set_mode((w_sc, h_sc))

clock = pygame.time.Clock()
running = True

# center of clock
x, y = w_sc/2, h_sc/2

# images
clock_img = pygame.image.load("clock.jpg")

s_img = pygame.image.load("short.png")
s_calibrated = 22 * 360/60
s_angle = s_calibrated

l_img = pygame.image.load("long.png")
l_calibrated = 25 * 360/60
l_angle = l_calibrated


def rotate(img, angle):
    w, h = img.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]

    box_rotate = [p.rotate(angle) for p in box]

    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    origin = (x + min_box[0], y - max_box[1])
    rotated_image = pygame.transform.rotate(img, angle)

    return rotated_image, origin


while running:
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(clock_img, (0, 0))

    sr = rotate(s_img, s_calibrated - minutes * 360/60)
    screen.blit(sr[0], sr[1])

    lr = rotate(l_img, l_calibrated - seconds * 360/60)
    screen.blit(lr[0], lr[1])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
