import pygame
import sys
from pygame import *
from math import *
import random
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

# universal settings
tile_size = 100
white = 255, 255, 255
black = 0, 0, 0
grey = 179, 179, 179


class Property:
    def __init__(self, name, price, base_rent):
        self.name = name
        self.price = price
        self.base_rent = base_rent
        self.owner = None

    def calculate_rent(self):
        if self.owner: 
            owned_properties = sum(1 for prop in property if prop.owner == self.owner)
            rent = self.base_rent * (2 ** (owned_properties - 1))
            return rent
        else:
            return 0


# Define property
property = [
    Property("Ramly Burger", 500, 10),
    Property("99 Minimarket", 600, 20),
    Property("Radio Televisyen Malaysia", 700, 35),
    Property("Astro", 750, 40),
    Property("Redhouse Melaka", 800, 50),
    Property("A'Famosa", 900, 55),
    Property("Jonker Street", 1000, 65),
    Property("Telekom Malaysia", 1200, 80),
    Property("Sky Bridge Langkawi", 1200, 85),
    Property("Penang Hill", 1400, 100),
    Property("George Town Penang", 1500, 110),
    Property("Chew Jetty", 1600, 120),
    Property("Cyberjaya", 1800, 140),
    Property("KL Central", 2000, 160),
    Property("Tenaga National Berhad", 2000, 160),
    Property("Cameroon Highland", 2200, 180),
    Property("Genting Highland", 2200, 180),
    Property("Putrajaya", 2400, 200),
    Property("KLIA", 2400, 200),
    Property("Lot10, Bukit Bintang", 2500, 220),
    Property("Pavilion Bukit Bintang", 2800, 240),
    Property("KL Tower", 3000, 275),
    Property("Merdeka 118", 3500, 350),
    Property("KLCC", 4000, 500)
]

# Pricelist = [500, 600, 700, 750, 800, 900, 1000, 1200, 1200, 1400, 1500, 1600,
#              1800, 2000, 2000, 2200, 2200, 2400, 2400, 2500, 2800, 3000, 3500, 4000]


class Display:
    text_font = pygame.font.Font("HelveticaNeue.ttf", 25)
    smaller_font = pygame.font.Font("HelveticaNeue.ttf", 20)
    Specia_font = pygame.font.SysFont(
        "ComicSansMS.ttf", 25, bold=False, italic=False)
    # text used in all the tile
    Go_t = text_font.render("Go", True, (white))
    collect_t = smaller_font.render("Pass & Go", True, (white))
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
    hill_1 = smaller_font.render("Penang", True, (grey))
    hill_2 = smaller_font.render("Hill", True, (grey))
    famosa_1 = smaller_font.render("A.Famosa", True, (grey))
    jonker_1 = smaller_font.render("Jonker", True, (grey))
    jonker_2 = smaller_font.render("Street", True, (grey))
    stadthuys_t = smaller_font.render("redhouse", True, (grey))
    astro_t = text_font.render("Astro", True, (black))
    rtm_t = text_font.render("RTM", True, (black))
    seven_t = text_font.render("7-11", True, (black))
    Ramly_t = smaller_font.render("B.Ramly", True, (black))
    # price_t = smaller_font.render(f"{Pricelist}", True, (white))
    # print(Pricelist)

    def showing_text():
        screen.blit(Display.klcc_t, (20, 120))
        screen.blit(Display.Go_t, (20, 20))
        # screen.blit(Display.price_t, (20, 20))
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
        screen.blit(Display.putra_t, (210, 720))
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
        screen.blit(Display.cyber_t, (810, 720))
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

        # drawing grids for maps

    def drawing_grid(tile_size):
        tile_size = 50*2
        for line in range(0, 10):
            pygame.draw.line(screen, (white), (0, line*tile_size),
                             (screen_width, line*tile_size))  # horizontal line

            pygame.draw.line(screen, (white), (line*tile_size, 0),
                             (line*tile_size, screen_height))  # vertical line

    def middle():
        rect_length = 800
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

    def checkmusic(self, position):
        if self.rect.collidepoint(position):
            self.toggleMusicState()

    def checkroll(self, position):
        if self.rect.collidepoint(position):
            dice_num = random.randint(1, 6)
            print(dice_num)

    def toggleMusicState(self):
        if self.is_music_on:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        self.is_music_on = not self.is_music_on


# Load button images
button_surface_on = pygame.image.load('pic/musicon.png')
button_surface_off = pygame.image.load('pic/musicoff.png')
button_roll = pygame.image.load('pic/Roll.png')
button_surface_on = pygame.transform.scale(button_surface_on, (40, 40))
button_surface_off = pygame.transform.scale(button_surface_off, (40, 40))
button_roll = pygame.transform.scale(button_roll, (80, 80))
button_music = Button(button_surface_on, button_surface_off, 650, 680)
button_roll = Button(button_roll, button_roll, 800, 650)


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


class Map:
    def __init__(self, data):
        self.tile_list = []
        white_box = pygame.image.load("pic/white box.png")
        yellow_box = pygame.image.load("pic/light yellow.png")
        green_box = pygame.image.load("pic/lightgreen.png")
        blue_box = pygame.image.load("pic/lightblue.png")
        purple_box = pygame.image.load("pic/lightpurple.png")
        red_box = pygame.image.load("pic/lightred.png")

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 2:
                    img = pygame.transform.scale(
                        white_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 4:
                    img = pygame.transform.scale(
                        yellow_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 5:
                    img = pygame.transform.scale(
                        green_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 6:
                    img = pygame.transform.scale(
                        blue_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 7:
                    img = pygame.transform.scale(
                        purple_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 8:
                    img = pygame.transform.scale(
                        red_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

        # loading image for the maps


class Player:
    def __init__(self, color, shape, row, col, scale_factor=0.5):
        self.color = color
        self.shape = shape
        self.row = row
        self.col = col
        self.scale_factor = scale_factor

    def draw(self):
        x = self.col * tile_size + tile_size//4
        y = self.row * tile_size + tile_size//4

        if self.shape == 'circle':
            radius = int(tile_size//4 * self.scale_factor)
            pygame.draw.circle(screen, self.color, (x, y), radius)
        elif self.shape == 'square':
            side_length = int(tile_size//2 * self.scale_factor)
            pygame.draw.rect(screen, self.color,
                             (x, y, side_length, side_length))
        elif self.shape == 'triangle':
            half_size = int(tile_size//2 * self.scale_factor)
            pygame.draw.polygon(screen, self.color, [(x + half_size, y),
                                                     (x, y + half_size),
                                                     (x + tile_size * self.scale_factor, y + half_size)])
        elif self.shape == 'star':
            star_size = int(tile_size//2 * self.scale_factor)
            pygame.draw.polygon(screen, self.color, [(x + star_size//2, y),
                                                     (x + star_size,
                                                      y + star_size),
                                                     (x, y + star_size//3),
                                                     (x + star_size,
                                                      y + star_size//3),
                                                     (x, y + star_size),
                                                     (x + star_size//2, y)])


player1 = Player((255, 0, 0), 'circle', 0, 0, scale_factor=0.5)
player2 = Player((0, 255, 0), 'square', 0, 0, scale_factor=0.5)
player3 = Player((0, 0, 255), 'triangle', 0, 0, scale_factor=0.5)
player4 = Player((255, 255, 0), 'star', 0, 0, scale_factor=0.5)

players = [player1, player2, player3, player4]


class economic:
    initial_money = int(1000)
    num_players = 4
    player_dict_m = {}
    for i in range(1, num_players+1):
        player_dict_m[f"p{i}_money"] = initial_money

    print(player_dict_m)


# Maps control for monopoly
map_data = [
    [1, 2, 2, 2, 2, 3, 4, 4, 4, 10],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 5],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 5],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 5],
    [29, 42, 43, 44, 45, 46, 47, 48, 49, 14],
    [7, 52, 53, 54, 55, 56, 57, 58, 59, 6],
    [7, 62, 63, 64, 65, 66, 67, 68, 69, 6],
    [26, 7, 7, 7, 7, 21, 6, 6, 6, 17],
]


map = Map(map_data)
# main run for game
run = True
while run:
    clock.tick(fps)
    screen.fill((0, 0, 0))
    map.draw()

    Display.middle()
    # Display.drawing_grid(100)

    # displaying text for all the tiles
    Display.showing_text()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_music.checkmusic(pygame.mouse.get_pos())
            button_roll.checkroll(pygame.mouse.get_pos())

    button_music.update()
    button_roll.update()

    pygame.display.update()
pygame.quit()
