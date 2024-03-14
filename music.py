import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True

songs = ["1.mp3", "2.mp3", "3.mp3", "4.mp3"]

current = 0
pygame.mixer.music.load(songs[current])
pygame.mixer.music.play(-1)
print("Q for play, W for stop, E for previous, R for next")
print(songs[current])


def play():
    pygame.mixer.music.play(-1)


def stop():
    pygame.mixer.music.stop()


def previous(curr):
    if curr == 0:
        curr = len(songs) - 1
    else:
        curr -= 1
    pygame.mixer.music.unload()
    pygame.mixer.music.load(songs[curr])
    pygame.mixer.music.play(-1)
    print(songs[curr])
    return curr


def following(curr):
    if curr == len(songs) - 1:
        curr = 0
    else:
        curr += 1
    pygame.mixer.music.unload()
    pygame.mixer.music.load(songs[curr])
    pygame.mixer.music.play(-1)
    print(songs[curr])
    return curr


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                play()
            if event.key == pygame.K_w:
                stop()
            if event.key == pygame.K_e:
                current = previous(current)
            if event.key == pygame.K_r:
                current = following(current)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()