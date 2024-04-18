import pygame
import math
import random
pygame.init()
#initiate pygame music features
pygame.mixer.init()
clock=pygame.time.Clock()
fps = 60

#differentiate different size for game window 
screen_width=800
screen_height=800
screen = pygame.display.set_mode((screen_width,screen_height))
# full_screen = pygame.display.set_mode((full_screen_W,fill_screen_H))
pygame.display.set_caption("Monopoly")

#image setting
background = pygame.image.load("pictures/blue.jpg")

#drawing grids for maps
def drawing_grid(tile_size):
    tile_size = 50*2
    for line in range (0,8):
        pygame.draw.line (screen,(255,255,255),(0,line*tile_size),(screen_width,line*tile_size))
        pygame.draw.line(screen,(255,255,255),(line*tile_size,0),(line*tile_size,screen_height))


#main run for game
run = True
while run:
    clock.tick(fps)
    pygame.display.flip()
    drawing_grid(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  

    pygame.display.update()
pygame.quit()

#anything