import pygame
import sys
from pygame.locals import *
pygame.init()
# initiate pygame music features
pygame.mixer.init()
clock = pygame.time.Clock()
fps = 60

# differentiate different size for game window
screen_width = 1000
screen_height = 800

pygame.display.set_caption("Monopoly")
screen = pygame.display.set_mode((screen_width, screen_height))


class Dice(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.animating = False
        self.sprites.append(pygame.image.load('pic/dice1.png'))
        self.sprites.append(pygame.image.load('pic/dice2.png'))
        self.sprites.append(pygame.image.load('pic/dice3.png'))
        self.sprites.append(pygame.image.load('pic/dice4.png'))
        self.sprites.append(pygame.image.load('pic/dice5.png'))
        self.sprites.append(pygame.image.load('pic/dice6.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.animating = True

    def update(self):
        if self.animating == True:
            self.current_sprite += 0.4

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            self.animating = False

        self.image = self.sprites[int(self.current_sprite)]


# create the sprites and groups
moving_sprites = pygame.sprite.Group()
dice = Dice(450, 350)
moving_sprites.add(dice)

run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            dice.animate()

    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)

    pygame.display.update()
pygame.quit()
