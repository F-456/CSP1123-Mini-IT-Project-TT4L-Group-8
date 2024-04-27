import pygame
import sys
from pygame import *
pygame.init()
# initiate pygame music features
pygame.mixer.init()
clock = pygame.time.Clock()
fps = 60

# differentiate different size for game window
screen_width = 800
screen_height = 800

pygame.display.set_caption("Monopoly")
screen = pygame.display.set_mode((screen_width, screen_height))

# universal settings
tile_size = 100
white = 255, 255, 255
grey = 179, 179, 179


class Display:
    text_font = pygame.font.Font(
        "HelveticaNeue.ttf", 25)
    smaller_font = pygame.font.Font("HelveticaNeue.ttf", 20)
    Specia_font = pygame.font.SysFont(
        "ComicSansMS.ttf", 25, bold=False, italic=False)
    # text used in all the tile
    Go_t = text_font.render("Go", True, (white))
    collect_t = smaller_font.render("Collect...", True, (white))
    klcc_t = text_font.render("KLCC", True, (white))
    money_t = smaller_font.render("$", True, (white))
    M118_t = text_font.render("M.118", True, (white))
    kl_t = text_font.render("kl.tower", True, (white))
    Q_t = text_font.render("?", True, (white))
    chance_t = smaller_font.render("Chance", True, (white))
    Pavilion_t = text_font.render("Pavilion", True, (white))
    Lot10_t = text_font.render("Lot10", True, (white))
    jail_t = text_font.render("Jail", True, (white))
    klia_t = text_font.render("KLIA", True, (white))
    cyber_t = smaller_font.render("Cyberjaya", True, (white))
    genting_t = smaller_font.render("G.highland", True, (white))
    cameroon_t = smaller_font.render("C.highland", True, (white))
    income_t = smaller_font.render("Income", True, (white))
    tax_t = smaller_font.render("tax", True, (white))
    tnb_t = text_font.render("TNB", True, (white))
    klsen_t = smaller_font.render("KL.central", True, (white))
    putra_t = smaller_font.render("Putrajaya", True, (white))
    Gojail1_t = smaller_font.render("Go to", True, (white))
    GOjail2_t = smaller_font.render("Jail", True, (white))
    chew1_t = smaller_font.render("Chew", True, (white))
    chew2_t = smaller_font.render("Jetty", True, (white))
    George1_t = smaller_font.render("Goerge", True, (white))
    George2_t = smaller_font.render("Town", True, (white))
    sky_t = smaller_font.render("Sky", True, (white))
    bridge_t = smaller_font.render("Bridge", True, (white))
    Tm_t = text_font.render("TM", True, (white))
    free_t = smaller_font.render("Free", True, (white))
    park_t = smaller_font.render("Parking", True, (white))
    hill_1 = smaller_font.render("Penang", True, (white))
    hill_2 = smaller_font.render("Hill", True, (white))
    famosa_1 = smaller_font.render("A.Famosa", True, (white))
    jonker_1 = smaller_font.render("Jonker", True, (white))
    jonker_2 = smaller_font.render("Street", True, (white))
    stadthuys_t = smaller_font.render("redhouse", True, (white))
    astro_t = text_font.render("Astro", True, (white))
    rtm_t = text_font.render("RTM", True, (white))
    seven_t = text_font.render("7-11", True, (white))
    Ramly_t = smaller_font.render("B.Ramly", True, (white))

    def showing_text():
        screen.blit(Display.klcc_t, (20, 120))
        screen.blit(Display.Go_t, (20, 20))
        screen.blit(Display.collect_t, (20, 50))
        screen.blit(Display.money_t, (20, 150))
        screen.blit(Display.M118_t, (20, 220))
        screen.blit(Display.money_t, (20, 250))
        screen.blit(Display.kl_t, (16, 320))
        screen.blit(Display.money_t, (20, 350))
        screen.blit(Display.Q_t, (40, 420))
        screen.blit(Display.chance_t, (20, 450))
        screen.blit(Display.Pavilion_t, (10, 520))
        screen.blit(Display.money_t, (20, 550))
        screen.blit(Display.Lot10_t, (20, 620))
        screen.blit(Display.money_t, (20, 650))
        screen.blit(Display.jail_t, (20, 720))
        screen.blit(Display.klia_t, (120, 720))
        screen.blit(Display.money_t, (120, 750))
        screen.blit(Display.cyber_t, (210, 720))
        screen.blit(Display.money_t, (220, 750))
        screen.blit(Display.genting_t, (305, 720))
        screen.blit(Display.money_t, (320, 750))
        screen.blit(Display.cameroon_t, (405, 720))
        screen.blit(Display.money_t, (420, 750))
        screen.blit(Display.income_t, (520, 720))
        screen.blit(Display.tax_t, (520, 750))
        screen.blit(Display.tnb_t, (620, 720))
        screen.blit(Display.money_t, (620, 750))
        screen.blit(Display.klsen_t, (710, 720))
        screen.blit(Display.money_t, (720, 750))
        screen.blit(Display.putra_t, (810, 720))
        screen.blit(Display.money_t, (820, 750))
        screen.blit(Display.Gojail1_t, (920, 720))
        screen.blit(Display.GOjail2_t, (930, 750))
        screen.blit(Display.chew1_t, (920, 610))
        screen.blit(Display.chew2_t, (920, 630))
        screen.blit(Display.money_t, (920, 650))
        screen.blit(Display.George1_t, (920, 510))
        screen.blit(Display.George2_t, (920, 530))
        screen.blit(Display.money_t, (920, 550))
        screen.blit(Display.Q_t, (950, 420))
        screen.blit(Display.chance_t, (920, 450))
        screen.blit(Display.hill_1, (920, 310))
        screen.blit(Display.hill_2, (920, 330))
        screen.blit(Display.money_t, (920, 350))
        screen.blit(Display.sky_t, (920, 210))
        screen.blit(Display.bridge_t, (920, 230))
        screen.blit(Display.money_t, (920, 250))
        screen.blit(Display.Tm_t, (920, 120))
        screen.blit(Display.money_t, (920, 150))
        screen.blit(Display.free_t, (920, 20))
        screen.blit(Display.park_t, (920, 50))
        screen.blit(Display.famosa_1, (710, 20))
        screen.blit(Display.money_t, (720, 50))
        screen.blit(Display.jonker_1, (820, 10))
        screen.blit(Display.jonker_2, (820, 30))
        screen.blit(Display.money_t, (820, 50))
        screen.blit(Display.stadthuys_t, (610, 20))
        screen.blit(Display.money_t, (620, 50))
        screen.blit(Display.income_t, (520, 20))
        screen.blit(Display.tax_t, (520, 50))
        screen.blit(Display.astro_t, (420, 20))
        screen.blit(Display.money_t, (420, 50))
        screen.blit(Display.rtm_t, (320, 20))
        screen.blit(Display.money_t, (320, 50))
        screen.blit(Display.seven_t, (220, 20))
        screen.blit(Display.money_t, (220, 50))
        screen.blit(Display.Ramly_t, (120, 20))
        screen.blit(Display.money_t, (120, 50))


# add background music
pygame.mixer.music.load('Sound/BGM.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops=-1, fade_ms=5000)

# Variable to track fade-in progress
fade_in_progress = True

# Check if the fade-in effect is complete
while fade_in_progress:
    if pygame.mixer.music.get_busy():
        current_volume = pygame.mixer.music.get_volume()
        if current_volume < 0.1:
            new_volume = min(current_volume + 0.01, 0.1)
            pygame.mixer.music.set_volume(new_volume)
        else:
            fade_in_progress = False


class Display():
    text_font = pygame.font.SysFont(
        "Arial", 25, bold=False, italic=True)
    smaller_font = pygame.font.SysFont("freesansbold.ttf", 25)
    Specia_font = pygame.font.SysFont("Arial", 25, bold=False, italic=False)

    def text_properties(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))
    # drawing grids for maps

    def drawing_grid(tile_size):
        tile_size = 50*2
        for line in range(0, 8):
            pygame.draw.line(screen, (white), (0, line*tile_size),
                             (screen_width, line*tile_size))  # horizontal line

            pygame.draw.line(screen, (white), (line*tile_size, 0),
                             (line*tile_size, screen_height))  # vertical line

    def middle():
        rect_length = 600
        rect_height = 600
        # align the main rect in the middle of screen
        rect_x = (screen_width - rect_length)/2
        rect_y = (screen_height - rect_height)/2
        Middle_rect = pygame.Rect(rect_x, rect_y, rect_length, rect_height)
        # minus the screen width to horizontal align the middle rect
        rect_colour = grey
        pygame.draw.rect(screen, (rect_colour), Middle_rect)


class Button():
    def __init__(self, image_on, image_off,  x_pos, y_pos):
        self.image_on = image_on
        self.image_off = image_off
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image_on.get_rect(center=(self.x_pos, self.y_pos))
        self.is_music_on = True

    def update(self):
        if self.is_music_on:
            screen.blit(self.image_on, self.rect)
        else:
            screen.blit(self.image_off, self.rect)

    def checkForInput(self, position):
        if self.rect.collidepoint(position):
            self.toggleMusicState()

    def toggleMusicState(self):
        if self.is_music_on:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        self.is_music_on = not self.is_music_on


# Load button images
button_surface_on = pygame.image.load('pic/musicon.png')
button_surface_off = pygame.image.load('pic/musicoff.png')
button_surface_on = pygame.transform.scale(button_surface_on, (40, 40))
button_surface_off = pygame.transform.scale(button_surface_off, (40, 40))
button = Button(button_surface_on, button_surface_off, 650, 680)


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
    [32, 12, 13, 14, 15, 16, 17, 18, 19, 11],
    [31, 22, 23, 24, 25, 26, 27, 28, 29, 12],
    [30, 32, 33, 34, 35, 36, 37, 38, 39, 13],
    [29, 42, 43, 44, 45, 46, 47, 48, 49, 14],
    [28, 52, 53, 54, 55, 56, 57, 58, 59, 15],
    [27, 62, 63, 64, 65, 66, 67, 68, 69, 16],
    [26, 25, 24, 23, 22, 21, 20, 19, 18, 17],
]

map = Map(map_data)

# main run for game
run = True
while run:
    clock.tick(fps)
    screen.fill((0, 0, 0))
    map.draw()

    Display.middle()
    Display.drawing_grid(100)

    # displaying text for all the tiles
    Display.showing_text()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.checkForInput(pygame.mouse.get_pos())

    button.update()

    pygame.display.update()
pygame.quit()
