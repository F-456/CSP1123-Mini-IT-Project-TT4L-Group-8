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

# add background music
pygame.mixer.music.load('Sound/BGM.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Define button parameters
button_width = 200
button_height = 50
button_x = (screen_width - button_width) // 2
button_y = screen_height - 100
button_color = (0, 255, 0)
button_text_color = (255, 255, 255)
button_font = pygame.font.Font(None, 36)
button_text = "Pause Music"
music_paused = False

#main run for game
run = True
while run:
    clock.tick(fps)
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    Display.middle()
    Display.drawing_grid(100)

    # Draw the music control button
    pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
    button_surface = button_font.render(button_text, True, button_text_color)
    screen.blit(button_surface, (button_x + 20, button_y + 10))

      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                if music_paused:
                    pygame.mixer.music.unpause()
                    button_text = "Pause Music"
                    music_paused = False
                else:
                    pygame.mixer.music.pause()
                    button_text = "Play Music"
                    music_paused = True

    pygame.display.update()
pygame.quit()

