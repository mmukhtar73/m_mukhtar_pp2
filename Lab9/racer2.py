
import random

import pygame

# setting global features
pygame.init()
HEIGHT, WIDTH = 600, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Street Racer')
CLOCK = pygame.time.Clock()

# loading background
background = pygame.image.load('Street.jpg')

# loading scores font
font_small = pygame.font.SysFont("Verdana", 20)


class Coin(pygame.sprite.Sprite):
    to_next = 0
    RARITY = 10

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin_50px.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (random.randint(0, WIDTH), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self):
        self.rect.move_ip(0, 10)

    @classmethod
    def can_add(cls):
        if cls.to_next >= 1:
            cls.to_next = cls.to_next - 1 + random.random() / cls.RARITY
            return True
        else:
            cls.to_next += random.random() / cls.RARITY


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width // 2, WIDTH - self.rect.width // 2), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.top > HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect.width // 2, WIDTH - self.rect.width // 2), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Racer.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if self.rect.left > 5 and pressed[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH - 5 and pressed[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)


def main():
    running = True

    # constant sprites for this level
    player = Player()
    enemy = Enemy()
    enemies = pygame.sprite.Group()
    enemies.add(enemy)
    coins = pygame.sprite.Group()
    score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # adding coins
        if Coin.can_add(): coins.add(Coin())
        
        # deleting coins
        for coin in coins:
            if coin.rect.top < HEIGHT: coin.move()
            else:
                coins.remove(coin)
                del coin

        enemy.move()
        player.update()

        # collision with enemies
        if pygame.sprite.spritecollideany(player, enemies):
            running = False

        # coin collection
        for coin in coins:
            if player.rect.colliderect(coin.rect):
                coins.remove(coin)
                del coin
                score += 1

        score_img = font_small.render(str(score), True, (0, 0, 0))
        score_rect = score_img.get_rect()
        score_rect.topright = (WIDTH - 10, 0)

        SCREEN.blit(background, (0, 0))
        player.draw(SCREEN)
        enemy.draw(SCREEN)
        for coin in coins:
            coin.draw(SCREEN)
        SCREEN.blit(score_img, score_rect)

        pygame.display.update()
        CLOCK.tick(30)


if __name__ == '__main__':
    main()
