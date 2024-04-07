import pygame
import math
import random
pygame.init()
#initiate pygame music features
pygame.mixer.init()
clock=pygame.time.Clock()
fps = 60

#differentiate different size for game window 
screen_width=1280
screen_height=720
full_screen_W=1920
fill_screen_H=1080
screen = pygame.display.set_mode((screen_width,screen_height))
# full_screen = pygame.display.set_mode((full_screen_W,fill_screen_H))
pygame.display.set_caption("Monopoly , please press F5 to switch to full screen mode")

#image setting
background = pygame.image.load("pictures/blue.jpg")


#main run for game
run = True
while run:
    clock.tick(fps)
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  

    pygame.display.update()
pygame.quit()