import pygame
from pygame.locals import *
pygame.init()
# initiate pygame music features
pygame.mixer.init()
clock = pygame.time.Clock()
fps = 60

# add background music
BGM = pygame.mixer.Sound("Sound/BGM.mp3")
BGM.set_volume(1.5)
# BGM.play()

# differentiate different size for game window
screen_width = 1000
screen_height = 800

pygame.display.set_caption("Monopoly")
screen = pygame.display.set_mode((screen_width, screen_height))


# universal settings
tile_size = 100
white = 255, 255, 255
grey = 179, 179, 179


class Display:
    text_font = pygame.font.SysFont(
        "Arial", 25, bold=False, italic=True)
    smaller_font = pygame.font.SysFont("freesansbold.ttf", 25)
    Specia_font = pygame.font.SysFont("Arial", 25, bold=False, italic=False)

    def text_properties(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))
    # drawing grids for maps

    def drawing_grid(tile_size):

        for line in range(0, 8):
            pygame.draw.line(
                screen, (white), (0, line *
                                  tile_size), (screen_width, line * tile_size)
            )  # horizontal line
        for line in range(0, 10):
            pygame.draw.line(
                screen,
                (white),
                (line * tile_size, 0),
                (line * tile_size, screen_height),
            )  # vertical line

    def middle():
        rect_length = 800
        rect_height = 600
        # align the main rect in the middle of screen
        rect_x = (screen_width - rect_length) / 2
        rect_y = (screen_height - rect_height) / 2
        Middle_rect = pygame.Rect(rect_x, rect_y, rect_length, rect_height)
        # minus the screen width to horizontal align the middle rect
        rect_colour = grey
        pygame.draw.rect(screen, (rect_colour), Middle_rect)


class Map:
    def __init__(self, data):
        self.tile_list = []
        klcc = pygame.image.load('pic/klcc.png')
        merdeka_118 = pygame.image.load('pic/merdeka.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 11:
                    pass
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

        # loading image for the maps


# maps for monopoly
map_data = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
    [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
    [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
]

map = Map(map_data)


# main run for game
run = True
while run:
    clock.tick(fps)
    Display.middle()
    map.draw()
    Display.drawing_grid(100)

    # displaying text for all the tiles
    Display.text_properties("Go", Display.text_font, (white), 20, 20)
    Display.text_properties(
        "Collect xxx ", Display.smaller_font, (white), 10, 50)
    Display.text_properties("KLCC", Display.text_font, (white), 20, 120)
    Display.text_properties("$", Display.smaller_font, (white), 20, 150)
    Display.text_properties("M .118", Display.text_font, (white), 20, 220)
    Display.text_properties("$", Display.smaller_font, (white), 20, 250)
    Display.text_properties("KL.Tower", Display.text_font, (white), 16, 320)
    Display.text_properties("$", Display.smaller_font, (white), 20, 350)
    Display.text_properties("?", Display.Specia_font, (white), 40, 420)
    Display.text_properties("Chance", Display.Specia_font, (white), 20, 450)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
