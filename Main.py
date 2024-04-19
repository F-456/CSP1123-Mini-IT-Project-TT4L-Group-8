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

pygame.display.set_caption("Monopoly")
screen = pygame.display.set_mode((screen_width,screen_height))
#image setting
background = pygame.image.load("pictures/blue.jpg")

#colour universal settings
white = 255,255,255
grey = 179, 179, 179

class Display():
#drawing grids for maps
    def drawing_grid(tile_size):
        tile_size = 50*2
        horizontal_cal = 0
        vertical_cal = 0
        for line in range (0,8):
            pygame.draw.line (screen,(white),(0,line*tile_size),(screen_width,line*tile_size)) #horizontal line

            pygame.draw.line(screen,(white),(line*tile_size,0),(line*tile_size,screen_height)) #vertical line

    def middle():
        rect_length = 600
        rect_height = 600
        #align the main rect in the middle of screen 
        rect_x = (screen_width - rect_length)/2
        rect_y = (screen_height - rect_height)/2
        Middle_rect=pygame.Rect(rect_x,rect_y,rect_length,rect_height)
        #minus the screen width to horizontal align the middle rect
        rect_colour = grey
        pygame.draw.rect(screen,(rect_colour),Middle_rect)

#main run for game
run = True
while run:
    clock.tick(fps)
    Display.middle()
    Display.drawing_grid(100)
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  

    pygame.display.update()
pygame.quit()

