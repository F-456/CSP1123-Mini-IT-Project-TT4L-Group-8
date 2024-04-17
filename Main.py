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

# full_screen = pygame.display.set_mode((full_screen_W,fill_screen_H))
pygame.display.set_caption("Monopoly , please press F4 to switch to full screen mode")

#image setting
background = pygame.image.load("pictures/blue.jpg")


#main run for game
run = True
while run:
    clock.tick(fps)
    screen = pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.K_F4:
            print("fullscreen")
            screen_width = 1920
            screen_height = 1080

        if event.type == pygame.QUIT:
            run = False  

    pygame.display.update()
pygame.quit()