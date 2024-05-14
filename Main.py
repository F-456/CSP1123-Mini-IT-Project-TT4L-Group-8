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
round_num = 1
num_row = 8
num_col = 10
white = 255, 255, 255
black = 0, 0, 0
grey = 179, 179, 179

text_font = pygame.font.Font("HelveticaNeue.ttf", 20)
smaller_font = pygame.font.Font("HelveticaNeue.ttf", 20)
Specia_font = pygame.font.SysFont(
    "ComicSansMS.ttf", 25, bold=False, italic=False)

# Maps control for monopoly
map_data = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [32, 0, 0, 0, 0, 0, 0, 0, 0, 11],
            [31, 0, 0, 0, 0, 0, 0, 0, 0, 12],
            [30, 0, 0, 0, 0, 0, 0, 0, 0, 13],
            [29, 0, 0, 0, 0, 0, 0, 0, 0, 14],
            [28, 0, 0, 0, 0, 0, 0, 0, 0, 15],
            [27, 0, 0, 0, 0, 0, 0, 0, 0, 16],
            [26, 25, 24, 23, 22, 21, 20, 19, 18, 17],
            ]

block_desctiptions = {
    2: "'Ramly burger', the most famous burger chain store in Malaysia",
    3: "'99 speedmarket', you can buy everything you want from here",
    4: "'Aeon Big'",
    6: "'Tenaga National Berhad(TNB)'",
    7: "'Batu Caves'",
    8: "'Pulau Langkawi'",
    9: "'Cameroon Highland'",
    11: "'Gunung Mulu'",
    12: "'Mount Kinabalu'",
    14: "'Johor Bahru'",
    15: "'George Town'",
    16: "'Melaka historical city'",
    18: "'KL Central’",
    19: "'Port Dickson'",
    20: "'MMU Cyberjaya'",
    22: "'Indah Water'",
    23: "'Genting Highland'",
    24: "'Putrajaya'",
    25: "'KLIA'",
    27: "'TRX'",
    28: "'Pavilion, KL'",
    30: "'KL Tower'",
    31: "'Merdeka 118'",
    32: "'KLCC'"
}


def display_descriptions(description):
    max_width = 400
    max_height = 300

    # Create a surface to render text
    description_surface = pygame.Surface((max_width, max_height))
    description_surface.fill(grey)

    font = pygame.font.Font(None, 36)
    text_lines = wrap_text(description, font, max_width)
    y_offset = 0
    for line in text_lines:
        text_surface = font.render(line, True, black)
        description_surface.blit(text_surface, (0, y_offset))
        y_offset += font.get_height()

    screen.blit(description_surface, (180, 150))
    pygame.display.flip()


def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ''
    for word in words:
        test_line = current_line + word + ' '
        test_line_surface = font.render(test_line, True, white)
        if test_line_surface.get_width() <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + ' '
    if current_line:
        lines.append(current_line)
    return lines


class Property:
    def __init__(self, name, price, base_rent):
        self.name = name
        self.price = price
        self.base_rent = base_rent
        self.owner = None

    def calculate_rent(self):
        if self.owner:
            owned_properties = sum(
                1 for prop in property if prop.owner == self.owner)
            rent = self.base_rent * (2 ** (owned_properties - 1))
            return rent
        else:
            return 0


# Define property
property = [
    Property("Ramly Burger", 500, 10),
    Property("99 Speedmarket", 600, 20),
    Property("Aeon Big", 700, 35),
    Property("TNB", 2100, 40),
    Property("Batu Caves", 800, 50),
    Property("Pulau Langkawi", 900, 55),
    Property("Cameron Highland", 1000, 65),
    Property("Gunung Mulu", 1200, 80),
    Property("Mount Kinabalu", 1300, 85),
    Property("Johor Bahru", 1400, 100),
    Property("George Town", 1500, 110),
    Property("Melaka", 1600, 120),
    Property("KL Sentral", 1800, 140),
    Property("Port Dickson", 2000, 160),
    Property("MMU Cyberjaya", 2000, 160),
    Property("Indah water", 2150, 180),
    Property("Genting Highland", 2200, 180),
    Property("Putrajaya", 2400, 200),
    Property("KLIA", 2500, 220),
    Property("TRX", 2600, 230),
    Property("Pavilion KL", 2800, 240),
    Property("KL Tower", 3000, 275),
    Property("Merdeka 118", 3500, 350),
    Property("KLCC", 4000, 500)
]

Pricelist = [0, 500, 600, 700, 0, 2100, 800, 900, 1000, 0, 1200, 1300, 0, 1400, 1500, 1600,
             0, 1800, 1900, 2000, 0, 2150, 2200, 2400, 2500, 0, 2600, 2800, 0, 3000, 3500, 4000]


class Display:
    text_font = pygame.font.Font("HelveticaNeue.ttf", 18)
    smaller_font = pygame.font.Font("HelveticaNeue.ttf", 18)
    Specia_font = pygame.font.SysFont(
        "ComicSansMS.ttf", 25, bold=False, italic=False)
    # text used in all the tile
    Go_t = text_font.render("Go", True, (white))
    collect_t = smaller_font.render("Pass & Go", True, (white))
    money_t = smaller_font.render("$", True, (black))
    klia_t = text_font.render("KLIA", True, (black))
    indah_t = smaller_font.render("Indah", True, (black))
    water_t = smaller_font.render("Water", True, (black))
    mmu_t = smaller_font.render("MMU", True, (black))
    cyber_t = smaller_font.render("Cyberjaya", True, (black))
    genting_t = smaller_font.render("Genting", True, (black))
    port_t = text_font.render("Port", True, (black))
    dickson_t = text_font.render("Dickson", True, (black))
    sen_t = smaller_font.render("Sentral", True, (black))
    putra_t = smaller_font.render("Putrajaya", True, (black))
    putra_t = smaller_font.render("Putrajaya", True, (black))
    kl_t = smaller_font.render("KL", True, (black))
    cameron_t = smaller_font.render("Cameron", True, (black))
    highland_t = smaller_font.render("Highland", True, (black))
    pulau_t = smaller_font.render("Pulau", True, (black))
    langkawi_t = smaller_font.render("Langkawi", True, (black))
    batu_caves_t = text_font.render("Batu Caves", True, (black))
    tnb_t = text_font.render("TNB", True, (black))
    aeon_t = text_font.render("AEON", True, (black))
    ninenine_t = text_font.render("99", True, (black))
    speedmarket_t = text_font.render("Market", True, (black))
    Ramly_t = smaller_font.render("B.Ramly", True, (black))
    price1_t = text_font.render("$ 500", True, (black))
    price2_t = text_font.render("$ 600", True, (black))
    price3_t = text_font.render("$ 700", True, (black))
    price4_t = text_font.render("$ 2100", True, (black))
    price5_t = text_font.render("$ 800", True, (black))
    price6_t = text_font.render("$ 900", True, (black))
    price7_t = text_font.render("$ 1000", True, (black))
    price8_t = text_font.render("$ 1800", True, (black))
    price9_t = text_font.render("$ 1900", True, (black))
    price10_t = text_font.render("$ 2000", True, (black))
    price11_t = text_font.render("$ 2150", True, (black))
    price12_t = text_font.render("$ 2200", True, (black))
    price13_t = text_font.render("$ 2400", True, (black))
    price14_t = text_font.render("$ 2500", True, (black))

    # price_t = smaller_font.render(f"{Pricelist}", True, (white))
    # print(Pricelist)

    def rotate_text(text, angle):
        return pygame.transform.rotate(text, angle)

    def render_rotate_text(font, text, color, angle):
        rotated_text = Display.rotate_text(
            font.render(text, True, color), angle)
        return rotated_text

    def showing_properties_name():
        screen.blit(Display.Go_t, (20, 20))
        screen.blit(Display.collect_t, (20, 50))
        klcc_rotated = Display.render_rotate_text(
            Display.text_font, "KLCC", (black), 270)
        screen.blit(klcc_rotated, (60, 125))
        klcc_price_rotated = Display.render_rotate_text(
            Display.text_font, "$ 4000", (black), 270)
        screen.blit(klcc_price_rotated, (20, 120))
        merdeka_rotated = Display.render_rotate_text(
            Display.text_font, "Merdeka", (black), 270)
        screen.blit(merdeka_rotated, (70, 215))
        m118_rotated = Display.render_rotate_text(
            Display.text_font, "118", (black), 270)
        screen.blit(m118_rotated, (50, 230))
        merdeka118_price_rotated = Display.render_rotate_text(
            Display.text_font, "$ 3500", (black), 270)
        screen.blit(merdeka118_price_rotated, (20, 220))
        kl_tower_rotated = Display.render_rotate_text(
            Display.text_font, "KL.Tower", (black), 270)
        screen.blit(kl_tower_rotated, (60, 310))
        kltower_price_rotated = Display.render_rotate_text(
            Display.text_font, "$ 3000", (black), 270)
        screen.blit(kltower_price_rotated, (20, 320))
        pavilion_rotated = Display.render_rotate_text(
            Display.text_font, "Pavilion", (black), 270)
        screen.blit(pavilion_rotated, (60, 515))
        pavilion_price_rotated = Display.render_rotate_text(
            Display.text_font, "$ 2800", (black), 270)
        screen.blit(pavilion_price_rotated, (20, 520))
        trx_rotated = Display.render_rotate_text(
            Display.text_font, "TRX", (black), 270)
        screen.blit(trx_rotated, (60, 625))
        trx_price_rotated = Display.render_rotate_text(
            Display.text_font, "$ 2600", (black), 270)
        screen.blit(trx_price_rotated, (20, 620))
        screen.blit(Display.klia_t, (132, 720))
        screen.blit(Display.price14_t, (123, 760))
        screen.blit(Display.putra_t, (212, 720))
        screen.blit(Display.price13_t, (223, 760))
        screen.blit(Display.genting_t, (320, 710))
        screen.blit(Display.highland_t, (315, 730))
        screen.blit(Display.price12_t, (323, 760))
        screen.blit(Display.indah_t, (425, 710))
        screen.blit(Display.water_t, (425, 730))
        screen.blit(Display.price11_t, (423, 760))
        screen.blit(Display.mmu_t, (630, 710))
        screen.blit(Display.cyber_t, (610, 730))
        screen.blit(Display.price10_t, (623, 760))
        screen.blit(Display.port_t, (733, 710))
        screen.blit(Display.dickson_t, (720, 730))
        screen.blit(Display.price9_t, (723, 760))
        screen.blit(Display.kl_t, (840, 710))
        screen.blit(Display.sen_t, (820, 730))
        screen.blit(Display.price8_t, (823, 760))
        melaka_rotated = Display.render_rotate_text(
            Display.text_font, "Melaka", (black), 90)
        screen.blit(melaka_rotated, (920, 620))
        melaka_price_rotated = Display.render_rotate_text(
            Display.text_font, "$ 1600", (black), 90)
        screen.blit(melaka_price_rotated, (960, 622))
        gtown1_rotated = Display.render_rotate_text(
            Display.text_font, "George", (black), 90)
        screen.blit(gtown1_rotated, (910, 520))
        gtown2_rotated = Display.render_rotate_text(
            Display.text_font, "Town", (black), 90)
        screen.blit(gtown2_rotated, (930, 530))
        gtown_price_rotated = Display.render_rotate_text(
            Display.text_font, "$ 1500", (black), 90)
        screen.blit(gtown_price_rotated, (960, 522))
        johot_rotated = Display.render_rotate_text(
            Display.text_font, "Johor", (black), 90)
        screen.blit(johot_rotated, (910, 425))
        bahru_rotated = Display.render_rotate_text(
            Display.text_font, "Bahru", (black), 90)
        screen.blit(bahru_rotated, (930, 425))
        jb_price_rotated = Display.render_rotate_text(
            Display.text_font, "$ 1400", (black), 90)
        screen.blit(jb_price_rotated, (960, 422))
        mount_rotated = Display.render_rotate_text(
            Display.text_font, "Mount", (black), 90)
        screen.blit(mount_rotated, (910, 220))
        kinabalu_rotated = Display.render_rotate_text(
            Display.text_font, "Kinabalu", (black), 90)
        screen.blit(kinabalu_rotated, (930, 213))
        mk_price_rotated = Display.render_rotate_text(
            Display.text_font, "$ 1300", (black), 90)
        screen.blit(mk_price_rotated, (960, 222))
        gunung_rotated = Display.render_rotate_text(
            Display.text_font, "Gunung", (black), 90)
        screen.blit(gunung_rotated, (910, 120))
        mulu_rotated = Display.render_rotate_text(
            Display.text_font, "Mulu", (black), 90)
        gm_price_rotated = Display.render_rotate_text(
            Display.text_font, "$ 1200", (black), 90)
        screen.blit(gm_price_rotated, (960, 122))
        screen.blit(mulu_rotated, (930, 130))
        screen.blit(Display.cameron_t, (815, 10))
        screen.blit(Display.highland_t, (815, 30))
        screen.blit(Display.price7_t, (823, 60))
        screen.blit(Display.pulau_t, (725, 10))
        screen.blit(Display.langkawi_t, (715, 30))
        screen.blit(Display.price6_t, (727, 60))
        screen.blit(Display.batu_caves_t, (604, 20))
        screen.blit(Display.price5_t, (627, 60))
        screen.blit(Display.tnb_t, (530, 20))
        screen.blit(Display.price4_t, (523, 60))
        screen.blit(Display.aeon_t, (323, 20))
        screen.blit(Display.price3_t, (327, 60))
        screen.blit(Display.ninenine_t, (240, 10))
        screen.blit(Display.speedmarket_t, (222, 30))
        screen.blit(Display.price2_t, (227, 60))
        screen.blit(Display.Ramly_t, (120, 20))
        screen.blit(Display.price1_t, (127, 60))

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
changing_round = False
buy_clicked = False


class Button():
    menu = True
    exit_game = False
    loading = True
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

    def checkload_finish(self, position):
        if self.rect.collidepoint(position):
            Button.loading = False

    def check_exit(self, position):
        if self.rect.collidepoint(position):
            Button.exit_game = True

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
button_exit = pygame.image.load('pic/exit.png')
button_next = pygame.image.load('pic/next.png')
button_buy = pygame.image.load('pic/buy.png')
# adjust size
button_surface_on = pygame.transform.scale(button_surface_on, (40, 40))
button_surface_off = pygame.transform.scale(button_surface_off, (40, 40))
button_roll = pygame.transform.scale(button_roll, (80, 80))
button_play = pygame.transform.scale(button_play, (240, 200))
button_exit = pygame.transform.scale(button_exit, (240, 200))
button_next = pygame.transform.scale(button_next, (120, 100))
button_buy = pygame.transform.scale(button_buy, (120, 100))
# adjust location
button_music = Button(button_surface_on, button_surface_off, 880, 120)
button_roll = Button(button_roll, button_roll, 800, 650)
button_play = Button(button_play, button_play, 700, 600)
button_exit = Button(button_exit, button_exit, 300, 600)
button_next = Button(button_next, button_next, 800, 600)
button_buy = Button(button_buy, button_buy, 800, 550)

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
        tax = pygame.image.load("pic/LHDN.png")
        injail = pygame.image.load("pic/injail.png")
        chance = pygame.image.load("pic/chance.png")

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

                elif tile == 3:
                    img = pygame.transform.scale(
                        white_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 4:
                    img = pygame.transform.scale(
                        white_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 5 or tile == 21:
                    img = pygame.transform.scale(
                        tax, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 6:
                    img = pygame.transform.scale(
                        yellow_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 7:
                    img = pygame.transform.scale(
                        yellow_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 8:
                    img = pygame.transform.scale(
                        yellow_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 9:
                    img = pygame.transform.scale(
                        yellow_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 11:
                    img = pygame.transform.scale(
                        yellow_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 12:
                    img = pygame.transform.scale(
                        yellow_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 13:
                    img = pygame.transform.scale(
                        chance, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 14:
                    img = pygame.transform.scale(
                        blue_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 15:
                    img = pygame.transform.scale(
                        blue_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 16:
                    img = pygame.transform.scale(
                        blue_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 18:
                    img = pygame.transform.scale(
                        blue_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 19:
                    img = pygame.transform.scale(
                        blue_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 20:
                    img = pygame.transform.scale(
                        blue_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 22:
                    img = pygame.transform.scale(
                        purple_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 23:
                    img = pygame.transform.scale(
                        purple_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 24:
                    img = pygame.transform.scale(
                        purple_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 25:
                    img = pygame.transform.scale(
                        purple_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 26:
                    img = pygame.transform.scale(
                        injail, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 27:
                    img = pygame.transform.scale(
                        purple_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 28:
                    img = pygame.transform.scale(
                        purple_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 29:
                    img = pygame.transform.scale(
                        chance, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 30:
                    img = pygame.transform.scale(
                        red_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 31:
                    img = pygame.transform.scale(
                        red_box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 32:
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


class Dice(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.animating = False
        self.num_frames = 6  # number of frames in animation sequence
        for i in range(1, 7):
            self.sprites.append(pygame.image.load(f'pic/dice{i}.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.animation_speed = 3
        self.animation_count = 0
        self.animation_max_count = 20

    def animate(self, dice_num):
        self.animating = True
        # Calculate the frame index corresponding to the roll value
        frame_index = min(dice_num - 1, self.num_frames - 1)
        # Update the current sprite to the frame corresponding to the roll
        self.current_sprite = frame_index
        self.image = self.sprites[self.current_sprite]

    def update(self):
        if self.animating:
            self.animation_count += self.animation_speed
            if self.animation_count >= self.animation_max_count:
                # Stop the animation when it reaches the target frame
                self.animating = False
                self.animation_max_count = 20  # Reset max count for future animations


# Create the sprite groups
moving_sprites = pygame.sprite.Group()

# Create the Dice sprite
dice = Dice(750, 350)
moving_sprites.add(dice)


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

    def move(self, steps):
        # Move the player along the perimeter of the grid
        for _ in range(steps):
            if self.row == 0 and self.col < num_col - 1:
                self.col += 1
            elif self.row < num_row - 1 and self.col == num_col - 1:
                self.row += 1
            elif self.row == num_row - 1 and self.col > 0:
                self.col -= 1
            elif self.row > 0 and self.col == 0:
                self.row -= 1

            # If the player reaches the starting position, stop
            # if self.row == 0 and self.col == 0:
            #     break

    def player_movement(dice_num):
        global dice_rolled,  player1_pos, player2_pos, player3_pos, player4_pos, player_sequence, changing_round, round_num
        player_sequence += 1

        if dice_con and dice_rolled and player_sequence == 1:
            dice_rolled = False
            print(f"dice is {dice_num}")
            player1_pos = player1_pos + dice_num
            changing_round = False
            if player1_pos < 32:
                print(f"Player 1 is now at:{player1_pos}")
            elif player1_pos == 32:
                player1_pos = 0
                print(f"Player 1 is now at: {player1_pos}")
            else:
                player1_pos -= 32
                print(f"Player 1 is now at: {player1_pos}")

        if dice_con and dice_rolled and player_sequence == 2:
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
        if dice_con and dice_rolled and player_sequence == 3:
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

        if dice_con and dice_rolled and player_sequence == 4:
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
            changing_round = True
            round_num += 1
            print(f'{round_num} round started')
            player_sequence -= 5


active_player_index = 0


player1 = Player((255, 0, 0), 'circle', 0, 0, scale_factor=0.5)
player2 = Player((0, 255, 0), 'square', 0, 0, scale_factor=0.5)
player3 = Player((0, 0, 255), 'triangle', 0, 0, scale_factor=0.5)
player4 = Player((255, 255, 0), 'star', 0, 0, scale_factor=0.5)
players = [player1, player2, player3, player4]


# settings for the property
price = 0
Pricelist = [0, 500, 600, 700, 0, 2100, 800, 900, 1000, 0, 1200, 1300, 0, 1400, 1500, 1600,
             0, 1800, 1900, 2000, 0, 2150, 2200, 2400, 2500, 0, 2600, 2800, 0, 3000, 3500, 4000]
b_property = str()

Property_with_price = {
    "Ramly Burger": 500,
    "99 Speedmarket": 600,
    "Aeon Big": 700,
    "TNB": 2100,
    "Batu Caves": 800,
    "Pulau Langkawi": 900,
    "Cameron Highland": 1000,
    "Gunung Mulu": 1200,
    "Mount Kinabalu": 1300,
    "Johor Bahru": 1400,
    "George Town": 1500,
    "Melaka": 1600,
    "KL Sentral": 1800,
    "Port Dickson": 1900,
    "MMU Cyberjaya": 2000,
    "Indah water": 2150,
    "Genting Highland": 2200,
    "Putrajaya": 2400,
    "KLIA": 2500,
    "TRX": 2600,
    "Pavilion KL": 2800,
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
        if player_sequence == 1 and player1_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            button_buy.update()

        elif player_sequence == 2 and player2_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            button_buy.update()

        elif player_sequence == 3 and player3_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            button_buy.update()

        elif player_sequence == 4 and player4_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
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
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    speed = 6
    text_done = False
    active_rules = 0
    title_font = pygame.font.Font("HelveticaNeue.ttf", 150)
    loading_font = pygame.font.Font("HelveticaNeue.ttf", 60)
    rule_font = pygame.font.Font("HelveticaNeue.ttf", 35)
    start_title = title_font.render("Pynopoly", True, (white))
    loading_title = loading_font.render("Loading...", True, (white))
    rules_1 = "This is a monopoly game"
    snip_rule1 = rule_font.render(
        'HelveticaNeue.ttf', True, white)
    rules_2 = "Game is played by 4 players"
    snip_rule2 = rule_font.render(
        'HelveticaNeue.ttf', True, white)
    rules_3 = "You'll need to expand and monopolized the whole game"
    snip_rule3 = rule_font.render(
        'HelveticaNeue.ttf', True, white)
    rules_4 = "If a player reach other's property, rent will be paid"
    snip_rule4 = rule_font.render(
        'HelveticaNeue.ttf', True, white)
    rules_5 = "The last player is winner"
    snip_rule5 = rule_font.render(
        'HelveticaNeue.ttf', True, white)
    rule_continue = rule_font.render(
        "Press the button to continue", True, (white))

    def title():
        screen.blit(starting_menu.start_title, (200, 100))

    def loading_screen():
        screen.blit(starting_menu.loading_title, (700, 700))

    def showing_rule():
        rule_num = 1
        # using function to modify typewritter displaying effect
        if rule_num == 1:
            if starting_menu.counter1 < starting_menu.speed * len(starting_menu.rules_1):
                starting_menu.counter1 += 1
            elif starting_menu.counter1 >= starting_menu.speed * len(starting_menu.rules_1):
                starting_menu.text_done = True
            snip_rule1 = starting_menu.rule_font.render(
                starting_menu.rules_1[0:starting_menu.counter1//starting_menu.speed], True, 'white')
            screen.blit(snip_rule1, (100, 100))
            if starting_menu.text_done:
                starting_menu.text_done = False
                rule_num += 1

        if rule_num == 2:
            if starting_menu.counter2 < starting_menu.speed * len(starting_menu.rules_2):
                starting_menu.counter2 += 1
            elif starting_menu.counter2 >= starting_menu.speed * len(starting_menu.rules_2):
                starting_menu.text_done = True
            snip_rule2 = starting_menu.rule_font.render(
                starting_menu.rules_2[0:starting_menu.counter2//starting_menu.speed], True, 'white')
            screen.blit(snip_rule2, (100, 160))
            if starting_menu.text_done:
                starting_menu.text_done = False
                rule_num += 1
        if rule_num == 3:
            if starting_menu.counter3 < starting_menu.speed * len(starting_menu.rules_3):
                starting_menu.counter3 += 1
            elif starting_menu.counter3 >= starting_menu.speed * len(starting_menu.rules_3):
                starting_menu.text_done = True
            snip_rule3 = starting_menu.rule_font.render(
                starting_menu.rules_3[0:starting_menu.counter3//starting_menu.speed], True, 'white')
            screen.blit(snip_rule3, (100, 220))
            if starting_menu.text_done:
                starting_menu.text_done = False
                rule_num += 1
        if rule_num == 4:
            if starting_menu.counter4 < starting_menu.speed * len(starting_menu.rules_4):
                starting_menu.counter4 += 1
            elif starting_menu.counter4 >= starting_menu.speed * len(starting_menu.rules_4):
                starting_menu.text_done = True
            snip_rule4 = starting_menu.rule_font.render(
                starting_menu.rules_4[0:starting_menu.counter4//starting_menu.speed], True, 'white')
            screen.blit(snip_rule4, (100, 280))
            if starting_menu.text_done:
                starting_menu.text_done = False
                rule_num += 1

        if rule_num == 5:
            if starting_menu.counter5 < starting_menu.speed * len(starting_menu.rules_5):
                starting_menu.counter5 += 1
            elif starting_menu.counter5 >= starting_menu.speed * len(starting_menu.rules_5):
                starting_menu.text_done = True
            snip_rule5 = starting_menu.rule_font.render(
                starting_menu.rules_5[0:starting_menu.counter5//starting_menu.speed], True, 'white')
            screen.blit(snip_rule5, (100, 340))
            if starting_menu.text_done:
                starting_menu.text_done = False
                rule_num += 1
        if rule_num == 6:
            screen.blit(starting_menu.rule_continue, (100, 400))


map = Map(map_data)


button_functions = [button_music.checkmusic, button_roll.checkroll,
                    button_play.check_play, button_buy.check_buy, button_next.checkload_finish, button_exit.check_exit]


def handle_button_events(pos):
    for button_function in button_functions:
        button_function(pos)


show_description = False
description = ""
description_display_duration = 20
description_display_timer = 0

# Modify the display_description_block function


def display_description_block(pos):
    global show_description, description, description_display_timer
    x, y = pos
    block_x, block_y = x // 100, y // 100
    block = map_data[block_y][block_x]
    if block in block_desctiptions:
        description = block_desctiptions[block]
        show_description = True
        description_display_timer = time.time()


run = True
# main loop for python
while run:
    clock.tick(fps)
    screen.fill((0, 0, 0))

    if Button.exit_game:
        run = False

    if Button.menu:
        button_play.update()
        button_exit.update()
        starting_menu.title()

    if not Button.menu and Button.loading:
        button_next.update()
        starting_menu.loading_screen()
        starting_menu.showing_rule()

    if not Button.menu and not Button.loading:
        # starting_menu.loading_screen()
        map.draw()
        Display.middle()
        Display.showing_properties_name()
        button_music.update()
        button_roll.update()
        economic.check_buying_valid()
        moving_sprites.draw(screen)
        moving_sprites.update()

        if show_description and time.time() - description_display_timer < description_display_duration:
            display_descriptions(description)
        else:
            show_description = False

        for player in players:
            player.draw()

        # Display.drawing_grid(100)
    else:
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_button_events(pygame.mouse.get_pos())
            display_description_block(pygame.mouse.get_pos())

        # if roll dice randomize a num
            if Button.rolling_con:
                rand_a_dice()
                dice_num = (random.randint(1, 6))
                # dice animating
                dice.animate(dice_num)
                Player.player_movement(dice_num)

                Button.rolling_con = False
                buy_clicked = False

                if player_sequence != 5 and not changing_round:
                    # Move the active player based on the dice roll
                    players[active_player_index].move(dice_num)
                    # Move to the next player
                    active_player_index = (
                        active_player_index + 1) % len(players)

            elif Button.is_buying_properties and not buy_clicked:
                economic.buying_property()

                buy_clicked = True
                Button.is_buying_properties == False
            else:
                pass

    pygame.display.update()
pygame.quit()
