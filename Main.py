import pygame
import sys
from pygame import *
from math import *
import random
import time
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

text_font = pygame.font.Font("HelveticaNeue.ttf", 20)
smaller_font = pygame.font.Font("HelveticaNeue.ttf", 20)
Specia_font = pygame.font.SysFont("ComicSansMS.ttf", 25, bold=False, italic=False)

    # Maps control for monopoly
map_data = [[1, 2, 2, 2, 2, 3, 4, 4, 4, 10],
            [8, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [8, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [8, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [29, 0, 0, 0, 0, 0, 0, 0, 0, 14],
            [7, 0, 0, 0, 0, 0, 0, 0, 0, 6],
            [7, 0, 0, 0, 0, 0, 0, 0, 0, 6],
            [26, 7, 7, 7, 7, 21, 6, 6, 6, 17],
]

block_desctiptions = {
    8 : "KLCC"
}


def display_descriptions(description):
    # Clear the screen
    font = pygame.font.Font(None, 36)
    # Display the description
    text_surface = font.render(description, True, white)
    screen.blit(text_surface, (200, 240))

    # Update the display
    pygame.display.flip()


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
    Property("Sky Bridge Langkawi", 1300, 85),
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


class Display:
    text_font = pygame.font.Font("HelveticaNeue.ttf", 20)
    smaller_font = pygame.font.Font("HelveticaNeue.ttf", 20)
    Specia_font = pygame.font.SysFont("ComicSansMS.ttf", 25, bold=False, italic=False)
    # text used in all the tile
    Go_t = text_font.render("Go", True, (white))
    collect_t = smaller_font.render("Pass & Go", True, (white))
    money_t = smaller_font.render("$", True, (black))
    Q_t = text_font.render("?", True, (white))
    chance_t = smaller_font.render("Chance", True, (white))
    jail_t = text_font.render("Jail", True, (white))
    klia_t = text_font.render("KLIA", True, (black))
    cyber_t = smaller_font.render("Cyberjaya", True, (black))
    genting_t = smaller_font.render("G.highland", True, (black))
    cameroon_t = smaller_font.render("C.highland", True, (black))
    income_t = smaller_font.render("Income", True, (white))
    tax_t = smaller_font.render("tax", True, (white))
    tnb_t = text_font.render("TNB", True, (black))
    klsen_t = smaller_font.render("KL.central", True, (black))
    putra_t = smaller_font.render("Putrajaya", True, (black))
    Gojail1_t = smaller_font.render("Go to", True, (white))
    GOjail2_t = smaller_font.render("Jail", True, (white))
    chew1_t = smaller_font.render("Chew", True, (black))
    chew2_t = smaller_font.render("Jetty", True, (black))
    George1_t = smaller_font.render("Goerge", True, (black))
    George2_t = smaller_font.render("Town", True, (black))
    sky_t = smaller_font.render("Sky", True, (black))
    bridge_t = smaller_font.render("Bridge", True, (black))
    Tm_t = text_font.render("TM", True, (black))
    free_t = smaller_font.render("Free", True, (white))
    park_t = smaller_font.render("Parking", True, (white))
    hill_1 = smaller_font.render("Penang", True, (black))
    hill_2 = smaller_font.render("Hill", True, (black))
    famosa_1 = smaller_font.render("A.Famosa", True, (black))
    jonker_1 = smaller_font.render("Jonker", True, (black))
    jonker_2 = smaller_font.render("Street", True, (black))
    stadthuys_t = smaller_font.render("redhouse", True, (black))
    astro_t = text_font.render("Astro", True, (black))
    rtm_t = text_font.render("RTM", True, (black))
    seven_t = text_font.render("99", True, (black))
    Ramly_t = smaller_font.render("B.Ramly", True, (black))
    # price_t = smaller_font.render(f"{Pricelist}", True, (white))
    # print(Pricelist)

    def rotate_text(text, angle):
        return pygame.transform.rotate(text, angle)
    
    def render_rotate_text(font, text, color, angle):
        rotated_text = Display.rotate_text(font.render(text, True, color),angle)
        return rotated_text

    def showing_properties_name():
        screen.blit(Display.Go_t, (20, 20))
        screen.blit(Display.collect_t, (20, 50))
        screen.blit(Display.Q_t, (40, 420))
        screen.blit(Display.chance_t, (20, 450))
        screen.blit(Display.jail_t, (20, 720))
        screen.blit(Display.income_t, (520, 720))
        screen.blit(Display.tax_t, (520, 750))
        screen.blit(Display.Q_t, (950, 420))
        screen.blit(Display.chance_t, (920, 450))
        screen.blit(Display.income_t, (520, 20))
        screen.blit(Display.tax_t, (520, 50))
        klcc_rotated = Display.render_rotate_text(Display.text_font, "KLCC", (black), 270)
        screen.blit(klcc_rotated, (55, 120))
        merdeka118_rotated = Display.render_rotate_text(Display.text_font, "M.118", (black), 270)
        screen.blit(merdeka118_rotated, (55, 220))
        kl_tower_rotated = Display.render_rotate_text(Display.text_font, "KL.Tower", (black), 270)
        screen.blit(kl_tower_rotated, (55, 310))
        pavilion_rotated = Display.render_rotate_text(Display.text_font, "Pavilion", (black), 270)
        screen.blit(pavilion_rotated, (55, 520))
        lot10_rotated = Display.render_rotate_text(Display.text_font, "Lot 10", (black), 270)
        screen.blit(lot10_rotated, (55, 620))
        screen.blit(Display.klia_t, (120, 720))
        screen.blit(Display.money_t, (120, 750))
        screen.blit(Display.putra_t, (210, 720))
        screen.blit(Display.money_t, (220, 750))
        screen.blit(Display.genting_t, (305, 720))
        screen.blit(Display.money_t, (320, 750))
        screen.blit(Display.cameroon_t, (405, 720))
        screen.blit(Display.money_t, (420, 750))
        screen.blit(Display.tnb_t, (620, 720))
        screen.blit(Display.money_t, (620, 750))
        screen.blit(Display.klsen_t, (710, 720))
        screen.blit(Display.money_t, (720, 750))
        screen.blit(Display.cyber_t, (810, 720))
        screen.blit(Display.money_t, (820, 750))
        chewjetty_rotated = Display.render_rotate_text(Display.text_font, "C.Jetty", (black), 90)
        screen.blit(chewjetty_rotated, (920, 620))
        gtown_rotated = Display.render_rotate_text(Display.text_font, "G.Town", (black), 90)
        screen.blit(gtown_rotated, (920, 520))
        PenangHill_rotated = Display.render_rotate_text(Display.text_font, "P.Hill", (black), 90)
        screen.blit(PenangHill_rotated, (920, 320))
        sky_b_rotated = Display.render_rotate_text(Display.text_font, "Sky.B", (black), 90)
        screen.blit(sky_b_rotated, (920, 220))
        tm_rotated = Display.render_rotate_text(Display.text_font, "TM", (black), 90)
        screen.blit(tm_rotated, (920, 120))
        screen.blit(Display.famosa_1, (710, 20))
        screen.blit(Display.money_t, (720, 50))
        screen.blit(Display.jonker_1, (820, 10))
        screen.blit(Display.jonker_2, (820, 30))
        screen.blit(Display.money_t, (820, 50))
        screen.blit(Display.stadthuys_t, (610, 20))
        screen.blit(Display.money_t, (620, 50))
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


# general value for button
dice_num = 0
dice_con = False
dice_rolled = False
buy_clicked = False


class Button():
    menu = True
    rolling_con = False
    is_buying_properties = False

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
            Button.rolling_con = True

    def check_play(self, position):
        if self.rect.collidepoint(position):
            Button.menu = False

    def check_buy(self, position):
        if self.rect.collidepoint(position):
            Button.is_buying_properties = True

    def toggleMusicState(self):
        if self.is_music_on:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        self.is_music_on = not self.is_music_on


def rand_a_dice():
    global dice_con, dice_rolled
    dice_rolled = True
    if not dice_con:
        dice_con = True
    return dice_rolled and dice_con == True


# Load button images
button_surface_on = pygame.image.load('pic/musicon.png')
button_surface_off = pygame.image.load('pic/musicoff.png')
button_roll = pygame.image.load('pic/Roll.png')
button_play = pygame.image.load('pic/play.png')
button_buy = pygame.image.load('pic/buy.png')
button_surface_on = pygame.transform.scale(button_surface_on, (40, 40))
button_surface_off = pygame.transform.scale(button_surface_off, (40, 40))
button_roll = pygame.transform.scale(button_roll, (80, 80))
button_play = pygame.transform.scale(button_play, (450, 170))
button_buy = pygame.transform.scale(button_buy, (100, 100))
button_music = Button(button_surface_on, button_surface_off, 880, 120)
button_roll = Button(button_roll, button_roll, 800, 650)
button_play = Button(button_play, button_play, 500, 400)
button_buy = Button(button_buy, button_buy, 800, 500)

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
        go_to_jail = pygame.image.load("pic/gotojail.webp")
        free_parking = pygame.image.load("pic/freeparking.png")

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

                elif tile == 8:
                    img = pygame.transform.scale(
                        red_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 10:
                    img = pygame.transform.scale(
                        free_parking, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 17:
                    img = pygame.transform.scale(
                        go_to_jail, (tile_size, tile_size))
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


# Global player position
player1_pos = 0
player2_pos = 0
player3_pos = 0
player4_pos = 0
# player sequence
player_sequence = 0


class Player:
    def __init__(self, color, shape, row, col, scale_factor=0.5):
        self.color = color
        self.shape = shape
        self.row = row
        self.col = col
        self.scale_factor = scale_factor
        self.dice_num = dice_num

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

    def player_movement(dice_num):
        global dice_rolled, player1_pos, player2_pos, player3_pos, player4_pos, player_sequence
        player_sequence += 1
        if dice_con and dice_rolled and player_sequence == 1:
            dice_rolled = False
            print(f"dice is {dice_num}")
            player1_pos = player1_pos + dice_num
            if player1_pos < 32:
                print(f"Player 1 is now at:{player1_pos}")
            elif player1_pos == 32:
                player1_pos = 0
                print(f"Player 1 is now at: {player1_pos}")
            else:
                player1_pos -= 32
                print(f"Player 1 is now at: {player1_pos}")

        elif dice_con and dice_rolled and player_sequence == 2:
            dice_rolled = False
            print(f"dice is {dice_num}")
            player2_pos = player2_pos + dice_num
            if player2_pos < 32:
                print(f"Player 2 is now at:{player2_pos}")
            elif player2_pos == 32:
                player2_pos = 0
                print(f"Player 2 is now at: {player2_pos}")
            else:
                player2_pos -= 32
                print(f"Player 2 is now at: {player2_pos}")
        elif dice_con and dice_rolled and player_sequence == 3:
            dice_rolled = False
            print(f"dice is {dice_num}")
            player3_pos = player3_pos + dice_num
            if player3_pos < 32:
                print(f"Player 3 is now at:{player3_pos}")
            elif player3_pos == 32:
                player3_pos = 0
                print(f"Player 3 is now at: {player3_pos}")
            else:
                player3_pos -= 32
                print(f"Player 3 is now at: {player3_pos}")

        elif dice_con and dice_rolled and player_sequence == 4:
            dice_rolled = False
            print(f"dice is {dice_num}")

            player4_pos = player4_pos + dice_num
            if player4_pos < 32:
                print(f"Player 4 is now at:{player4_pos}")
            elif player4_pos == 32:
                player4_pos = 0
                print(f"Player 4 is now at: {player4_pos}")
            else:
                player4_pos -= 32
                print(f"Player 4 is now at: {player4_pos}")

        elif player_sequence == 5:
            print('next_round')
            player_sequence -= 5


player1 = Player((255, 0, 0), 'circle', 0, 0, scale_factor=0.5)
player2 = Player((0, 255, 0), 'square', 0, 0, scale_factor=0.5)
player3 = Player((0, 0, 255), 'triangle', 0, 0, scale_factor=0.5)
player4 = Player((255, 255, 0), 'star', 0, 0, scale_factor=0.5)
players = [player1, player2, player3, player4]


# settings for the property
price = 0
Pricelist = [0, 500, 600, 700, 750, 0, 800, 900, 1000, 0, 1200, 1200, 1400, 0, 1500,  1600,
             1800, 0, 2000, 2000, 2200, 0, 2200, 2400, 2400, 0, 2500, 2800, 0, 3000, 3500, 4000]
b_property = str()

Property_with_price = {
    "Ramly Burger": 500,
    "99 Minimarket": 600,
    "Radio Televisyen Malaysia": 700,
    "Astro": 750,
    "Redhouse Melaka": 800,
    "A'Famosa": 900,
    "Jonker Street": 1000,
    "Telekom Malaysia": 1200,
    "Sky Bridge Langkawi": 1300,
    "Penang Hill": 1400,
    "George Town Penang": 1500,
    "Chew Jetty": 1600,
    "Cyberjaya": 1800,
    "KL Central": 2000,
    "Tenaga National Berhad": 2000,
    "Cameroon Highland": 2200,
    "Genting Highland": 2200,
    "Putrajaya": 2400,
    "KLIA": 2400,
    "Lot10, Bukit Bintang": 2500,
    "Pavilion Bukit Bintang": 2800,
    "KL Tower": 3000,
    "Merdeka 118": 3500,
    "KLCC": 4000
}

# setting for player
initial_money = int(15000)
player_dict_m = {'p1_money': initial_money, 'p2_money': initial_money,
                 'p3_money': initial_money, 'p4_money': initial_money}
p1_list_p = []
p2_list_p = []
p3_list_p = []
p4_list_p = []
player1_broke = False
player2_broke = False
player3_broke = False
player4_broke = False


class economic:
    # checking for validity in buying property
    # player will not be able to click buy button if tile is not available to sell

    def check_buying_valid():
        if player_sequence == 1 and player1_pos not in [0, 5, 9, 13, 16, 20, 25, 28]:
            button_buy.update()

        elif player_sequence == 2 and player2_pos not in [0, 5, 9, 13, 16, 20, 25, 28]:
            button_buy.update()

        elif player_sequence == 3 and player3_pos not in [0, 5, 9, 13, 16, 20, 25, 28]:
            button_buy.update()

        elif player_sequence == 4 and player4_pos not in [0, 5, 9, 13, 16, 20, 25, 28]:
            button_buy.update()

        else:
            pass

    def buying_property():

        if player_sequence == 1 and player1_broke == False:
            price = Pricelist[player1_pos]
            print(f"price ={price}")
            before_buy_p1 = player_dict_m['p1_money']
            player_dict_m['p1_money'] = before_buy_p1 - price
            after_buy_p1 = player_dict_m['p1_money']
            print(f'Player1 now have {after_buy_p1}$')

        elif player_sequence == 2 and player2_broke == False:
            price = Pricelist[player2_pos]
            print(f"price ={price}")
            before_buy_p2 = player_dict_m['p2_money']
            player_dict_m['p2_money'] = before_buy_p2 - price
            after_buy_p2 = player_dict_m['p2_money']
            print(f'Player2 now have {after_buy_p2}$')

        elif player_sequence == 3 and player3_broke == False:
            price = Pricelist[player3_pos]
            print(f"price ={price}")
            before_buy_p3 = player_dict_m['p3_money']
            player_dict_m['p3_money'] = before_buy_p3 - price
            after_buy_p3 = player_dict_m['p3_money']
            print(f'Player3 now have {after_buy_p3}$')

        elif player_sequence == 4 and player4_broke == False:
            price = Pricelist[player4_pos]
            print(f"price ={price}")
            before_buy_p4 = player_dict_m['p4_money']
            player_dict_m['p4_money'] = before_buy_p4 - price
            after_buy_p4 = player_dict_m['p4_money']
            print(f'Player4 now have {after_buy_p4}$')

        else:
            price = 0
            pass

        economic.owning_property(price)

    def owning_property(price):
        if player_sequence == 1 and Pricelist[player1_pos] != 0:
            b_property = [
                i for i in Property_with_price if Property_with_price[i] == price]

            p1_list_p.append(b_property)
            print(f'player 1 now have {p1_list_p}')
            Pricelist[player1_pos] = 0
        elif player_sequence == 2 and Pricelist[player2_pos] != 0:
            b_property = [
                i for i in Property_with_price if Property_with_price[i] == price]

            p2_list_p.append(b_property)
            print(f'player 2 now have {p2_list_p}')
            Pricelist[player2_pos] = 0
        elif player_sequence == 3 and Pricelist[player3_pos] != 0:
            b_property = [
                i for i in Property_with_price if Property_with_price[i] == price]

            p3_list_p.append(b_property)
            print(f'player 3 now have {p3_list_p}')
            Pricelist[player3_pos] = 0
        elif player_sequence == 4 and Pricelist[player4_pos] != 0:
            b_property = [
                i for i in Property_with_price if Property_with_price[i] == price]

            p4_list_p.append(b_property)
            print(f'player 4 now have {p4_list_p}')
            Pricelist[player4_pos] = 0

    print(player_dict_m)


class starting_menu:
    title_font = pygame.font.Font("HelveticaNeue.ttf", 150)
    start_title = title_font.render("Pynopoly", True, (white))

    def title():
        screen.blit(starting_menu.start_title, (200, 100))

map = Map(map_data)
# main run for game
run = True

while run:
    clock.tick(fps)
    screen.fill((0, 0, 0))
    button_play.update()
    starting_menu.title()

    if not Button.menu:
        map.draw()
        Display.middle()
        Display.showing_properties_name()
        button_music.update()
        button_roll.update()
        economic.check_buying_valid()

        # Display.drawing_grid(100)
    else:
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_music.checkmusic(pygame.mouse.get_pos())
            button_roll.checkroll(pygame.mouse.get_pos())
            button_play.check_play(pygame.mouse.get_pos())
            button_buy.check_buy(pygame.mouse.get_pos())
            if event.button == 1:  # Left mouse button
                x, y = pygame.mouse.get_pos()
                block_x, block_y = x // 100, y // 100
                block = map_data[block_y][block_x]
                if block in block_desctiptions:
                    description = block_desctiptions[block]
                    display_descriptions(description)

        # if roll dice randomize a num
            if Button.rolling_con:
                rand_a_dice()
                Player.player_movement(random.randint(1, 6))
                Button.rolling_con = False
                buy_clicked = False

            elif Button.is_buying_properties and not buy_clicked:
                economic.buying_property()

                buy_clicked = True
                Button.is_buying_properties == False
            else:
                pass

    pygame.display.update()
pygame.quit()
