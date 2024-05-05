import pygame
import random
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

pygame.display.set_caption("Dice")
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

        self.animation_speed = 1
        self.animation_count = 0 
        self.animation_max_count = 20

    def animate(self):
        self.animating = True

    def update(self):
        if self.animating == True:
            self.animation_count += self.animation_speed

            if self.animation_count >= self.animation_max_count:
                self.current_sprite = random.randint(0, 5)
                self.image = self.sprites[self.current_sprite]
                self.animation = 0
                self.animation_max_count -= self.animation_speed
                
                if self.animation_max_count <= 0:
                    self.animating = False
                    self.animation_max_count = 20


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
