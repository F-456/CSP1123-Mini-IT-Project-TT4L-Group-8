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

pygame.display.set_caption("Pynopoly")
screen = pygame.display.set_mode((screen_width, screen_height))

# universal settings
tile_size = 100
round_num = 1
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
    2:pygame.image.load('pic/klcc.png').convert_alpha,
    3:pygame.image.load('pic/klcc.png').convert_alpha,
    4:pygame.image.load('pic/klcc.png').convert_alpha,
    6:pygame.image.load('pic/klcc.png').convert_alpha,
    7:pygame.image.load('pic/klcc.png').convert_alpha,
    8:pygame.image.load('pic/klcc.png').convert_alpha,
    9:pygame.image.load('pic/klcc.png').convert_alpha,
    11:pygame.image.load('pic/klcc.png').convert_alpha,
    12:pygame.image.load('pic/klcc.png').convert_alpha,
    14:pygame.image.load('pic/klcc.png').convert_alpha,
    15:pygame.image.load('pic/klcc.png').convert_alpha,
    16:pygame.image.load('pic/klcc.png').convert_alpha,
    18:pygame.image.load('pic/klcc.png').convert_alpha,
    19:pygame.image.load('pic/klcc.png').convert_alpha,
    20:pygame.image.load('pic/klcc.png').convert_alpha,
    22:pygame.image.load('pic/klcc.png').convert_alpha,
    23:pygame.image.load('pic/klcc.png').convert_alpha,
    24:pygame.image.load('pic/klcc.png').convert_alpha,
    25:pygame.image.load('pic/klcc.png').convert_alpha,
    27:pygame.image.load('pic/klcc.png').convert_alpha,
    28:pygame.image.load('pic/klcc.png').convert_alpha,
    30:pygame.image.load('pic/klcc.png').convert_alpha,
    31:pygame.image.load('pic/klcc.png').convert_alpha,
    32:pygame.image.load('pic/klcc.png').convert_alpha
}


def display_descriptions():
    max_width = 500
    max_height = 350

    # Create a surface to render text
    description_surface = pygame.Surface((max_width, max_height))
    description_surface.fill(grey)

    image = pygame.image.load('pic/klcc.png')
    image_rect = image.get_rect()
    image_rect.top = 0
    image_rect.left = 0
    description_surface.blit(image, image_rect)

    # font = pygame.font.Font("HelveticaNeue.ttf", 24)
    # text_lines = wrap_text(description, font, max_width)
    # y_offset = 0
    # for line in text_lines:
    #     text_surface = font.render(line, True, black)
    #     description_surface.blit(text_surface, (0, y_offset))
    #     y_offset += font.get_height()

    screen.blit(description_surface, (180, 150))
    pygame.display.flip()


# def wrap_text(text, font, max_width):
#     words = text.split(' ')
#     lines = []
#     current_line = ''
#     for word in words:
#         test_line = current_line + word + ' '
#         test_line_surface = font.render(test_line, True, white)
#         if test_line_surface.get_width() <= max_width:
#             current_line = test_line
#         else:
#             lines.append(current_line)
#             current_line = word + ' '
#     if current_line:
#         lines.append(current_line)
#     return lines


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
    current_player = current_round = int()
    player1_money = player2_money = player3_money = player4_money = str()
    activity = str()
    current_player = current_round = int()
    player1_money = player2_money = player3_money = player4_money = str()
    activity = str()
    # displaying image
    players_num_image = pygame.transform.scale(pygame.image.load(
        'pic/chooseplayer.png').convert_alpha(), (1000, 800))
    players_num_image_rect = players_num_image.get_rect(
        center=(screen_width//2, screen_height//2))
    players_num_image = pygame.transform.scale(pygame.image.load(
        'pic/chooseplayer.png').convert_alpha(), (1000, 800))
    players_num_image_rect = players_num_image.get_rect(
        center=(screen_width//2, screen_height//2))
    show_players_image = pygame.transform.scale(pygame.image.load(
        'pic/loading background.png').convert_alpha(), (1000, 800))
    show_players_image_rect = show_players_image.get_rect(
        center=(screen_width//2, screen_height//2))
    show_load_bool = True
    limit = 0
    alpha = 0
    show_loading_done = False
    # adding a boolean to control the function to loop one times

    def show_player_explain():
        # adding a limit to control when the if expression end
        Display.limit += 1
        if Display.show_load_bool and Display.alpha <= 255:
            # adjusting the value to adjust the appear speed
            Display.alpha += 0.9
            if Display.limit >= 300 or Display.alpha >= 255:
                Display.show_load_bool = False
        if not Display.show_load_bool and not Display.show_loading_done:
            # adjusting the value to adjust the disappear speed
            Display.alpha -= 3
        if Display.alpha <= 0:
            Display.show_loading_done = True
        print(Display.alpha)
        Display.show_players_image.set_alpha(Display.alpha)
        screen.blit(Display.show_players_image,
                    Display.show_players_image_rect)

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
        screen.blit(trx_rotated, (60, 630))
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
    # grid for demonstrating not using in normal play
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

    def showing_player_round():
        text_font = pygame.font.Font("HelveticaNeue.ttf", 22)
        if player_sequence != 0:
            current_player = text_font.render(
                f"Player {player_sequence} turn", True, black)
            screen.blit(current_player, (100, 110))
            # showing which round of current when player sequence is 0
        elif player_sequence == 0:
            Display.current_round = round_num
            current_player = text_font.render(
                f"Current round = {Display.current_round}", True, (black))
            screen.blit(current_player, (100, 110))

    def showing_player_money():
        text_font = pygame.font.Font("HelveticaNeue.ttf", 22)
        if not player1_broke:
            Display.player1_money = text_font.render(
                f'Player 1 now have {player_dict_m["p1_money"]} $', True, black)
        # showing player 1 info if he is broke
        if player1_broke:
            Display.player1_money = text_font.render(
                f'Player 1 is broke', True, black)
        if not player2_broke:
            Display.player2_money = text_font.render(
                f'Player 2 now have {player_dict_m["p2_money"]} $', True, black)
        if player2_broke:
            Display.player2_money = text_font.render(
                f'Player 2 is broke', True, black)
        if not player3_broke:
            Display.player3_money = text_font.render(
                f'Player 3 now have {player_dict_m["p3_money"]} $', True, black)
        if player3_broke:
            Display.player3_money = text_font.render(
                f'Player 3 is broke', True, black)
        if not player4_broke:
            Display.player4_money = text_font.render(
                f'Player 4 now have {player_dict_m["p4_money"]} $', True, black)
        if player4_broke:
            Display.player4_money = text_font.render(
                f'Player 4 is broke', True, black)

        screen.blit(Display.player1_money, (580, 110))
        screen.blit(Display.player2_money, (580, 140))
        if not player_num2:
            screen.blit(Display.player3_money, (580, 170))
        if not player_num2 and not player_num3:
            screen.blit(Display.player4_money, (580, 200))

    def showing_dim_button():
        button_pay_dim.update()
        button_buy_dim.update()
        button_chance_dim.update()
        button_upgrade_dim.update()

    # showing last activity by player
    def showing_activity():
        showing_activity = str()
        text_font = pygame.font.Font("HelveticaNeue.ttf", 18)
        showing_activity = text_font.render(Display.activity, True, black)
        screen.blit(showing_activity, (110, 650))


# general value for button
dice_num = 0
dice_con = False
dice_rolled = False
changing_round = False
buy_clicked = False
pay_clicked = False
paying = False


class Button():
    global paying
    menu = True
    player_choose = False
    exit_game = False
    loading = True
    rolling_con = False
    is_buying_properties = False
    is_paying_rent = False
    # is_upgrade_properties = False

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
        if self.rect.collidepoint(position) and economic.showing_buy_button:
            if not Button.is_buying_properties:
                economic.buying_property()

    def check_pay(self, position):
        if self.rect.collidepoint(position):
            Button.is_paying_rent = True
            if player_sequence == 1:
                economic.rent_button_1()
            if player_sequence == 2:
                economic.rent_button_2()
            if player_sequence == 3:
                economic.rent_button_3()
            if player_sequence == 4:
                economic.rent_button_4()
    
    # def check_upgrade(self, position):
    #     if self.rect.collidepoint(position):
    #         Button.is_upgrade_properties = True

    def check_chance(self, position):
        if self.rect.collidepoint(position) and not Chance.chance_done:
            print('chance chance')
            Chance.chance_done = True
            if player_sequence == 1:
                Chance.chance_button1()
            if player_sequence == 2:
                Chance.chance_button2()
            if player_sequence == 3:
                Chance.chance_button3()
            if player_sequence == 4:
                Chance.chance_button4()

    def check_upgrade(self, position):
        if self.rect.collidepoint(position) and not economic.upgrading:
            print('upgrade property')
            economic.upgrading = True
            if player_sequence == 1:
                economic.upgrade_player1()
            if player_sequence == 2:
                economic.upgrade_player2()
            if player_sequence == 3:
                economic.upgrade_player3()
            if player_sequence == 4:
                economic.upgrade_player4()

    def player_num_2(self, position):
        global player_num2
        if self.rect.collidepoint(position) and not Button.player_choose and not Button.loading:
            print('Select player number 2')
            Button.player_choose = True
            player_num2 = True

    def player_num_3(self, position):
        global player_num3
        if self.rect.collidepoint(position) and not Button.player_choose and not Button.loading:
            print('Select player number 3')
            Button.player_choose = True
            player_num3 = True

    def player_num_4(self, position):
        if self.rect.collidepoint(position) and not Button.player_choose and not Button.loading:
            print('Select player number 4')
            Button.player_choose = True

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
button_play = pygame.image.load('pic/play.png')
button_exit = pygame.image.load('pic/exit.png')
button_next = pygame.image.load('pic/next.png')
button_buy = pygame.image.load('pic/buy.png')
button_buy_dim = pygame.image.load('pic/buy_dim.png')
button_pay = pygame.image.load('pic/pay.png')
button_pay_dim = pygame.image.load('pic/pay_dim.png')
button_chance = pygame.image.load('pic/chance_b.png')
button_chance_dim = pygame.image.load('pic/chance_dim.png')
button_upgrade = pygame.image.load('pic/upgrade.png')
button_upgrade_dim = pygame.image.load('pic/upgrade_dim.png')
button_2p = pygame.image.load('pic/2P.png')
button_3p = pygame.image.load('pic/3P.png')
button_4p = pygame.image.load('pic/4P.png')


# adjust size
button_surface_on = pygame.transform.scale(button_surface_on, (40, 40))
button_surface_off = pygame.transform.scale(button_surface_off, (40, 40))
button_roll = pygame.transform.scale(button_roll, (84, 56))
button_play = pygame.transform.scale(button_play, (240, 150))
button_pay = pygame.transform.scale(button_pay, (84, 56))
button_pay_dim = pygame.transform.scale(button_pay_dim, (84, 56))
button_exit = pygame.transform.scale(button_exit, (240, 150))
button_next = pygame.transform.scale(button_next, (120, 100))
button_buy = pygame.transform.scale(button_buy, (84, 56))
button_buy_dim = pygame.transform.scale(button_buy_dim, (84, 56))
button_chance = pygame.transform.scale(button_chance, (84, 56))
button_chance_dim = pygame.transform.scale(button_chance_dim, (84, 56))
button_upgrade = pygame.transform.scale(button_upgrade, (84, 56))
button_upgrade_dim = pygame.transform.scale(button_upgrade_dim, (84, 56))
button_2p = pygame.transform.scale(button_2p, (300, 200))
button_3p = pygame.transform.scale(button_3p, (300, 200))
button_4p = pygame.transform.scale(button_4p, (300, 200))

# adjust location
button_music = Button(button_surface_on, button_surface_off, 880, 120)
button_roll = Button(button_roll, button_roll, 660, 650)
button_play = Button(button_play, button_play, 700, 600)
button_exit = Button(button_exit, button_exit, 300, 600)
button_next = Button(button_next, button_next, 800, 600)
button_buy = Button(button_buy, button_buy, 830, 650)
button_buy_dim = Button(button_buy_dim, button_buy_dim, 830, 650)
button_pay = Button(button_pay, button_pay, 745, 650)
button_pay_dim = Button(button_pay_dim, button_pay_dim, 745, 650)
button_chance = Button(button_chance, button_chance, 575, 650)
button_chance_dim = Button(button_chance_dim, button_chance_dim, 575, 650)
button_upgrade = Button(button_upgrade, button_upgrade, 490, 650)
button_upgrade_dim = Button(button_upgrade_dim, button_upgrade_dim, 490, 650)
button_2p = Button(button_2p, button_2p, 500, 600)
button_3p = Button(button_3p, button_3p, 500, 450)
button_4p = Button(button_4p, button_4p, 500, 300)

# add background music
pygame.mixer.music.load('Sound/BGM.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=-1, fade_ms=5000)

# Variable to track fade-in progress
fade_in_progress = True

# Check if the fade-in effect is complete
while fade_in_progress:
    if pygame.mixer.music.get_busy():
        current_volume = pygame.mixer.music.get_volume()
        if current_volume < 0.01:
            new_volume = min(current_volume + 0.01, 0.001)
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

    def rand_a_dice():
        global dice_con, dice_rolled
        dice_rolled = True
        if not dice_con:
            dice_con = True
        return dice_rolled and dice_con == True

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
dice = Dice(500, 350)
moving_sprites.add(dice)


class Player:
    pic1 = pygame.image.load('pic/player1.png').convert_alpha()
    pic2 = pygame.image.load('pic/player2.png').convert_alpha()
    pic3 = pygame.image.load('pic/player3.png').convert_alpha()
    pic4 = pygame.image.load('pic/player4.png').convert_alpha()
    w1 = pic1.get_width()
    h1 = pic1.get_height()
    w2 = pic2.get_width()
    h2 = pic2.get_height()
    w3 = pic3.get_width()
    h3 = pic3.get_height()
    w4 = pic4.get_width()
    h4 = pic4.get_height()
    x1 = y1 = x2 = y2 = x3 = y3 = x4 = y4 = 0
    playerlist_4 = ['Player1', 'Player2', 'Player3', 'Player4']
    playerlist_3 = ['Player1', 'Player2', 'Player3']
    playerlist_2 = ['Player1', 'Player2']
    player1_in_jail = False
    player1_jail_round = 0
    player2_in_jail = False
    player2_jail_round = 0
    player3_in_jail = False
    player3_jail_round = 0
    player4_in_jail = False
    player4_jail_round = 0

    p1 = pygame.transform.scale(pic1, (int(w1 * 0.35), int(h1 * 0.35)))
    p2 = pygame.transform.scale(pic2, (int(w2 * 0.35), int(h2 * 0.35)))
    p3 = pygame.transform.scale(pic3, (int(w3 * 0.35), int(h3 * 0.35)))
    p4 = pygame.transform.scale(pic4, (int(w4 * 0.35), int(h4 * 0.35)))

    def __init__(self, image, player_name, index):
        self.image = image
        self.rect = self.image.get_rect()
        self.dice_num = dice_num
        self.player_name = player_name
        self.index = index

    def move(dice_num):
        step = int(0)
        step = dice_num
        second_step = int(0)
        global player_sequence
        # check whether the player is in the first row and move
        if player_sequence == 1 and not Player.player1_in_jail:
            if Player.x1 < 1000 and Player.y1 == 0:
                Player.x1 += step * 100
                # check if player exceed x boundary and needed to turn down
                if Player.x1 >= 1000:
                    second_step = Player.x1 - 1000
                    Player.x1 = 900
                    Player.y1 += second_step + 100

            elif Player.x1 == 900 and Player.y1 != 0:
                Player.y1 += step * 100
                if Player.y1 >= 800:
                    second_step = Player.y1 - 800
                    Player.y1 = 700
                    Player.x1 -= second_step
                    Player.x1 -= 100

            elif Player.x1 < 1000 and Player.y1 == 700:
                Player.x1 -= step * 100
                if Player.x1 <= 0:
                    second_step = 0 - Player.x1
                    Player.x1 = 0
                    Player.y1 = 700 - second_step

            elif Player.x1 == 0 and Player.y1 <= 700:
                Player.y1 -= step * 100
                if Player.y1 <= 0:
                    second_step = 0 - Player.y1
                    Player.y1 = 0
                    Player.x1 = second_step
        elif Player.player1_in_jail:
            Player.x1 = 0
            Player.y1 = 700

        if player_sequence == 2 and not Player.player2_in_jail:
            if Player.x2 < 1000 and Player.y2 == 0:
                Player.x2 += step * 100
                if Player.x2 >= 1000:
                    second_step = Player.x2 - 1000
                    Player.x2 = 900
                    Player.y2 += second_step + 100

            elif Player.x2 == 900 and Player.y2 != 0:
                Player.y2 += step * 100
                if Player.y2 >= 800:
                    second_step = Player.y2 - 800
                    Player.y2 = 700
                    Player.x2 -= second_step
                    Player.x2 -= 100

            elif Player.x2 < 1000 and Player.y2 == 700:
                Player.x2 -= step * 100
                if Player.x2 <= 0:
                    second_step = 0 - Player.x2
                    Player.x2 = 0
                    Player.y2 = 700 - second_step

            elif Player.x2 == 0 and Player.y2 <= 700:
                Player.y2 -= step * 100
                if Player.y2 <= 0:
                    second_step = 0 - Player.y2
                    Player.y2 = 0
                    Player.x2 = second_step
        elif Player.player2_in_jail:
            Player.x2 = 0
            Player.y2 = 700

        if player_sequence == 3 and not Player.player3_in_jail:
            if Player.x3 < 1000 and Player.y3 == 0:
                Player.x3 += step * 100
                if Player.x3 >= 1000:
                    second_step = Player.x3 - 1000
                    Player.x3 = 900
                    Player.y3 += second_step + 100

            elif Player.x3 == 900 and Player.y3 != 0:
                Player.y3 += step * 100
                if Player.y3 >= 800:
                    second_step = Player.y3 - 800
                    Player.y3 = 700
                    Player.x3 -= second_step
                    Player.x3 -= 100

            elif Player.x3 < 1000 and Player.y3 == 700:
                Player.x3 -= step * 100
                if Player.x3 <= 0:
                    second_step = 0 - Player.x3
                    Player.x3 = 0
                    Player.y3 = 700 - second_step

            elif Player.x3 == 0 and Player.y3 <= 700:
                Player.y3 -= step * 100
                if Player.y3 <= 0:
                    second_step = 0 - Player.y3
                    Player.y3 = 0
                    Player.x3 = second_step
        elif Player.player3_in_jail:
            Player.x3 = 0
            Player.y3 = 700

        if player_sequence == 4 and not Player.player4_in_jail:
            if Player.x4 < 1000 and Player.y4 == 0:
                Player.x4 += step * 100
                if Player.x4 >= 1000:
                    second_step = Player.x4 - 1000
                    Player.x4 = 900
                    Player.y4 += second_step + 100

            elif Player.x4 == 900 and Player.y4 != 0:
                Player.y4 += step * 100
                if Player.y4 >= 800:
                    second_step = Player.y4 - 800
                    Player.y4 = 700
                    Player.x4 -= second_step
                    Player.x4 -= 100

            elif Player.x4 < 1000 and Player.y4 == 700:
                Player.x4 -= step * 100
                if Player.x4 <= 0:
                    second_step = 0 - Player.x4
                    Player.x4 = 0
                    Player.y4 = 700 - second_step

            elif Player.x4 == 0 and Player.y4 <= 700:
                Player.y4 -= step * 100
                if Player.y4 <= 0:
                    second_step = 0 - Player.y4
                    Player.y4 = 0
                    Player.x4 = second_step
        elif Player.player4_in_jail:
            Player.x4 = 0
            Player.y4 = 700

    def show_players():
        global player_num2, player_num3
        if not player1_broke:
            screen.blit(Player.p1, (Player.x1, Player.y1))
        if not player2_broke:
            screen.blit(Player.p2, (Player.x2, Player.y2))
        if not player_num2 and not player3_broke:
            screen.blit(Player.p3, (Player.x3, Player.y3))
        if not player_num3 and not player_num2 and not player4_broke:
            screen.blit(Player.p4, (Player.x4, Player.y4))

    def player_movement(dice_num):
        global dice_rolled,  player1_pos, player2_pos, player3_pos, player4_pos, player_sequence, changing_round, round_num
        player_sequence += 1
        if dice_con and dice_rolled and player_sequence == 1 and not Player.player1_in_jail:
            dice_rolled = False
            print(f"dice is {dice_num}")
            player1_pos = player1_pos + dice_num
            changing_round = False
            # detecting if a player is in jail tile
            if player1_pos == 16:
                Player.player_jail1()
            # detecting if a player is in tax tile
            if player1_pos == 4 or player1_pos == 20:
                economic.tax()
            # a player position is less than a new round
            elif player1_pos < 32:
                print(f"Player 1 is now at:{player1_pos}")
            # a player position goes back on the origin and reset it to 0
            elif player1_pos == 32:
                player1_pos = 0
                player_dict_m['p1_money'] += 2000
                print(f"player 1 passes go and get 2000")
                print(f"Player 1 is now at: {player1_pos}")

            else:
                # a player position exceed total tile of a round , therefore -32 to adjust to new lapse
                player1_pos -= 32
                player_dict_m['p1_money'] += 2000
                print(f"player 1 passes go and get 2000")
                print(f"Player 1 is now at: {player1_pos}")

        if dice_con and dice_rolled and player_sequence == 2 and not Player.player2_in_jail:
            dice_rolled = False
            print(f"dice is {dice_num}")
            player2_pos = player2_pos + dice_num
            if player2_pos == 16:
                Player.player_jail2()
            if player2_pos == 4 or player2_pos == 20:
                economic.tax()
            elif player2_pos < 32:
                print(f"Player 2 is now at:{player2_pos}")
            elif player2_pos == 32:
                player2_pos = 0
                player_dict_m['p2_money'] += 2000
                print(f"player 2 passes go and get 2000")
                print(f"Player 2 is now at: {player2_pos}")

            else:
                player2_pos -= 32
                player_dict_m['p2_money'] += 2000
                print(f"player 2 passes go and get 2000")
                print(f"Player 2 is now at: {player2_pos}")
        if dice_con and dice_rolled and player_sequence == 3 and not Player.player3_in_jail:
            dice_rolled = False
            print(f"dice is {dice_num}")
            player3_pos = player3_pos + dice_num
            if player3_pos == 16:
                Player.player_jail3()
            if player3_pos == 4 or player3_pos == 20:
                economic.tax()
            elif player3_pos < 32:
                print(f"Player 3 is now at:{player3_pos}")
            elif player3_pos == 32:
                player3_pos = 0
                player_dict_m['p3_money'] += 2000
                print(f"player 3 passes go and added 2000")
                print(f"Player 3 is now at: {player3_pos}")
            else:
                player3_pos -= 32
                player_dict_m['p3_money'] += 2000
                print(f"player 3 passes go and added 2000")
                print(f"Player 3 is now at: {player3_pos}")

        if dice_con and dice_rolled and player_sequence == 4 and not Player.player4_in_jail:
            dice_rolled = False
            print(f"dice is {dice_num}")
            player4_pos = player4_pos + dice_num
            if player4_pos == 16:
                Player.player_jail4()
            if player4_pos == 4 or player4_pos == 20:
                economic.tax()
            elif player4_pos < 32:
                print(f"Player 4 is now at:{player4_pos}")
            elif player4_pos == 32:
                player4_pos = 0
                player_dict_m['p4_money'] += 2000
                print(f"player 4 passes go and added 2000")
                print(f"Player 4 is now at: {player4_pos}")
            else:
                player4_pos -= 32
                player_dict_m['p4_money'] += 2000
                print(f"player 4 passes go and added 2000")
                print(f"Player 4 is now at: {player4_pos}")

        elif player_sequence == 5:
            changing_round = True
            round_num += 1
            print(f'{round_num} round started')
            player_sequence -= 5

            # if a new round started check whether if a player is in jail and count a round for his sentences
            if Player.player1_in_jail:
                Player.player1_jail_sentences()
            if Player.player2_in_jail:
                Player.player2_jail_sentences()
            if Player.player3_in_jail:
                Player.player3_jail_sentences()
            if Player.player4_in_jail:
                Player.player4_jail_sentences()

    def player_jail1():
        global player1_pos
        # run a def and switch a bool to true and stop moving a certain player
        print('player 1 in jail')
        # adjusting position of a player
        player1_pos = 25
        Player.player1_in_jail = True

    def player_jail2():
        global player2_pos
        print('player 2 in jail')
        player2_pos = 25
        Player.player2_in_jail = True

    def player_jail3():
        global player3_pos
        print('player 3 in jail')
        player3_pos = 25
        Player.player3_in_jail = True

    def player_jail4():
        global player4_pos
        print('player 4 in jail')
        player4_pos = 25
        Player.player4_in_jail = True

    def player1_jail_sentences():
        # checking if the player has passed two round since being jailed and set the player free
        if Player.player1_jail_round == 1:
            Player.player1_in_jail = False
            Player.player1_jail_round -= 1
        else:
            Player.player1_jail_round += 1
            print('Player1 is 1 more round from freedom')

    def player2_jail_sentences():
        if Player.player2_jail_round == 1:
            Player.player2_in_jail = False
            Player.player2_jail_round -= 1
        else:
            Player.player2_jail_round += 1
            print('Player2 is 1 more round from freedom')

    def player3_jail_sentences():
        if Player.player3_jail_round == 1:
            Player.player3_in_jail = False
            Player.player3_jail_round -= 1
        else:
            Player.player3_jail_round += 1
            print('Player3 is 1 more round from freedom')

    def player4_jail_sentences():
        if Player.player4_jail_round == 1:
            Player.player4_in_jail = False
            Player.player4_jail_round -= 1
        else:
            Player.player4_jail_round += 1
            print('Player4 is 1 more round from freedom')

    def player_check_broke():
        global player1_broke, player2_broke, player3_broke, player4_broke, p1_broked, p2_broked, p3_broked, p4_broked
        if player_dict_m["p1_money"] < 0 and not p1_broked:
            player1_broke = True
            p1_broked = True
            print('Player 1 is broke')
        if player_dict_m["p2_money"] < 0 and not p2_broked:
            player2_broke = True
            p2_broked = True
            print('Player 2 is broke')
        if player_dict_m["p3_money"] < 0 and not p3_broked:
            player3_broke = True
            p3_broked = True
            print('Player 3 is broke')
            Display.activity = (f'Player 3 is broke')
        if player_dict_m["p4_money"] < 0 and not p4_broked:
            player4_broke = True
            p4_broked = True
            print('Player 4 is broke')

    def player_check_win():
        if not player_num2 and not player_num3:
            Player.player_check_win_4()
        if player_num3:
            Player.player_check_win_3()
        if player_num2:
            Player.player_check_win_2()

    def player_check_win_4():
        if player1_broke:
            if 'Player1' in Player.playerlist_4:
                Player.playerlist_4.remove('Player1')
        if player2_broke:
            if 'Player2' in Player.playerlist_4:
                Player.playerlist_4.remove('Player2')
        if player3_broke:
            if 'Player3' in Player.playerlist_4:
                Player.playerlist_4.remove('Player3')
        if player4_broke:
            if 'Player4' in Player.playerlist_4:
                Player.playerlist_4.remove('Player4')

        if len(Player.playerlist_4) == 1:
            winner = Player.playerlist_4[0]
            print(f"The winner is {winner}")
            Display.activity = (f'The winner is {winner} !!')

    def player_check_win_3():
        if player1_broke:
            if 'Player1' in Player.playerlist_3:
                Player.playerlist_3.remove('Player1')
        if player2_broke:
            if 'Player2' in Player.playerlist_3:
                Player.playerlist_3.remove('Player2')
        if player3_broke:
            if 'Player3' in Player.playerlist_3:
                Player.playerlist_3.remove('Player3')

        if len(Player.playerlist_3) == 1:
            winner = Player.playerlist_3[0]
            print(f"The winner is {winner}")
            Display.activity = (f'The winner is {winner} !!')

    def player_check_win_2():
        if player1_broke:
            if 'Player1' in Player.playerlist_2:
                Player.playerlist_2.remove('Player1')
        if player2_broke:
            if 'Player2' in Player.playerlist_2:
                Player.playerlist_2.remove('Player2')

        if len(Player.playerlist_2) == 1:
            winner = Player.playerlist_2[0]
            print(f"The winner is {winner}")
            Display.activity = (f'The winner is {winner} !!')


player_names = ["player1", "player2", "player3", "player4"]

# Create player instances
player1 = (Player.p1, "Player 1", 1)
player2 = (Player.p2, "Player 2", 2)
player3 = (Player.p3, "Player 3", 3)
player4 = (Player.p4, "Player 4", 4)

players = [player1, player2, player3, player4]

chance_rarities = {
    "Common": [
        "Advance to GO. Collect $300",
        "It is your birthday. Collect $100 from each player",
        "Go back to B.Ramly"
    ],
    "Rare": [
        "Advance to Free parking. If you pass Go, collect $200.",
        "Bank pays you dividend of $300.",
        "Go to jail, move directly to jail,do not collect $200",
    ],
    "Epic": [
        "Advance one step forward and rest. If the property is owned, no payment is required. If unclaimed, you have the option to purchase it from the bank. ",
        "Seize any property of your choosing.",
        "hired hacker cunningly snatches $200 from each player.",
        "Experience the unexpected tremors of an earthquake, resulting in each player losing $1500.",
    ]
}


class Chance:
    showing_chance = False
    chance_done = False
    player1_c = False
    player2_c = False
    player3_c = False
    player4_c = False

    def determine_chance_rarity(second_roll):
        if second_roll >= 5:
            return "Epic"
        elif second_roll >= 3:
            return "Rare"
        else:
            return "Common"

    def handle_chance():
        if player_sequence == 0:
            if player1_pos == 12 or player1_pos == 28:
                second_roll = random.randint(1, 6)
                chance_rarity = Chance.determine_chance_rarity(second_roll)

    def determine_chance_rarity(second_roll):
        if second_roll >= 5:
            return "Epic"
        elif second_roll >= 3:
            return "Rare"
        else:
            return "Common"

    def check_chance_valid():

        if not Chance.chance_done:
            if player1_pos == 12 or player1_pos == 28:
                Chance.showing_chance = True
                Chance.player1_c = True
            if player2_pos == 12 or player2_pos == 28:
                Chance.showing_chance = True
                Chance.player2_c = True
            if player3_pos == 12 or player3_pos == 28:
                Chance.showing_chance = True
                Chance.player3_c = True
            if player4_pos == 12 or player4_pos == 28:
                Chance.showing_chance = True
                Chance.player4_c = True
        else:
            Chance.showing_chance = False
        Chance.player_leave_chance()
    # detect whether a player who get chance leave the position and reset to make button disappear

    def player_leave_chance():
        if Chance.player1_c:
            if player1_pos != 12 and player1_pos != 28:
                Chance.chance_done = False
                Chance.player1_c = False
        if Chance.player2_c:
            if player2_pos != 12 and player2_pos != 28:
                Chance.chance_done = False
                Chance.player2_c = False
        if Chance.player3_c:
            if player3_pos != 12 and player3_pos != 28:
                Chance.chance_done = False
                Chance.player3_c = False
        if Chance.player4_c:
            if player4_pos != 12 and player4_pos != 28:
                Chance.chance_done = False
                Chance.player4_c = False

    def chance_button1():
        if player_sequence == 1:
            second_roll = random.randint(1, 6)
            chance_rarity = Chance.determine_chance_rarity(second_roll)
            chance_card = random.choice(chance_rarities[chance_rarity])
            print("Player 1 draws a", chance_rarity,
                  "chance card:", chance_card)
            if "Advance to GO" in chance_card:
                Player.x1 = 0
                Player.y1 = 0
            elif "Collect $100 from each player" in chance_card:
                pass
            elif "Go back to B.Ramly" in chance_card:
                Player.x1 = 100
                Player.y1 = 0
            elif "Advance to Free parking" in chance_card:
                Player.x1 = 900
                Player.y1 = 0
            elif "Bank pays you dividend of $300" in chance_card:
                pass
            elif "Go to jail" in chance_card:
                Player.x1 = 0
                Player.y1 = 700
            elif "Advance one step forward and rest" in chance_card:
                if Player.x1 < 1000 and Player.y1 == 0:
                    Player.x1 + 100
                elif Player.x1 == 900 and Player.y1 != 0:
                    Player.y1 + 100

                elif Player.x1 < 1000 and Player.y1 == 700:
                    Player.x1 - 100
                elif Player.x1 == 0 and Player.y1 <= 700:
                    Player.y1 - 100
            elif "Seize any property" in chance_card:
                pass
            elif "snatches $200 from each player" in chance_card:
                pass
            elif "earthquake" in chance_card:
                pass

            Chance.chance_done = True

    def chance_button2():
        if player_sequence == 2:
            second_roll = random.randint(1, 6)
            chance_rarity = Chance.determine_chance_rarity(second_roll)
            chance_card = random.choice(chance_rarities[chance_rarity])
            print("Player 2 draws a", chance_rarity,
                  "chance card:", chance_card)
            if "Advance to GO" in chance_card:
                Player.x2 = 0
                Player.y2 = 0
            elif "Collect $100 from each player" in chance_card:
                pass
            elif "Go back to B.Ramly" in chance_card:
                Player.x2 = 100
                Player.y2 = 0
            elif "Advance to Free parking" in chance_card:
                Player.x2 = 900
                Player.y2 = 0
            elif "Bank pays you dividend of $300" in chance_card:
                pass
            elif "Go to jail" in chance_card:
                Player.x2 = 0
                Player.y2 = 700
            elif "Advance one step forward and rest" in chance_card:
                if Player.x2 < 1000 and Player.y2 == 0:
                    Player.x2 + 100
                elif Player.x2 == 900 and Player.y2 != 0:
                    Player.y2 + 100

                elif Player.x2 < 1000 and Player.y2 == 700:
                    Player.x2 - 100
                elif Player.x2 == 0 and Player.y2 <= 700:
                    Player.y2 - 100
            elif "Seize any property" in chance_card:
                pass
            elif "snatches $200 from each player" in chance_card:
                pass
            elif "earthquake" in chance_card:
                pass

            Chance.chance_done = True

    def chance_button3():
        if player_sequence == 3:
            second_roll = random.randint(1, 6)
            chance_rarity = Chance.determine_chance_rarity(second_roll)
            chance_card = random.choice(chance_rarities[chance_rarity])
            print("Player 3 draws a", chance_rarity,
                  "chance card:", chance_card)
            if "Advance to GO" in chance_card:
                Player.x3 = 0
                Player.y3 = 0
            elif "Collect $100 from each player" in chance_card:
                pass
            elif "Go back to B.Ramly" in chance_card:
                Player.x3 = 100
                Player.y3 = 0
            elif "Advance to Free parking" in chance_card:
                Player.x3 = 900
                Player.y3 = 0
            elif "Bank pays you dividend of $300" in chance_card:
                pass
            elif "Go to jail" in chance_card:
                Player.x3 = 0
                Player.y3 = 700
            elif "Advance one step forward and rest" in chance_card:
                if Player.x3 < 1000 and Player.y3 == 0:
                    Player.x3 + 100
                elif Player.x3 == 900 and Player.y3 != 0:

                    Player.y3 + 100
                elif Player.x3 < 1000 and Player.y3 == 700:
                    Player.x3 - 100
                elif Player.x3 == 0 and Player.y3 <= 700:
                    Player.y3 - 100
            elif "Seize any property" in chance_card:
                pass
            elif "snatches $200 from each player" in chance_card:
                pass
            elif "earthquake" in chance_card:
                pass
            Chance.chance_done = True

    def chance_button4():
        if player_sequence == 4:
            second_roll = random.randint(1, 6)
            chance_rarity = Chance.determine_chance_rarity(second_roll)
            chance_card = random.choice(chance_rarities[chance_rarity])
            print("Player 4 draws a", chance_rarity,
                  "chance card:", chance_card)
            if "Advance to GO" in chance_card:
                Player.x4 = 0
                Player.y4 = 0
            elif "Collect $100 from each player" in chance_card:
                pass
            elif "Go back to B.Ramly" in chance_card:
                Player.x4 = 100
                Player.y4 = 0
            elif "Advance to Free parking" in chance_card:
                Player.x4 = 900
                Player.y4 = 0
            elif "Bank pays you dividend of $300" in chance_card:
                pass
            elif "Go to jail" in chance_card:
                Player.x4 = 0
                Player.y4 = 700
            elif "Advance one step forward and rest" in chance_card:
                if Player.x4 < 1000 and Player.y4 == 0:
                    Player.x4 + 100
                elif Player.x4 == 900 and Player.y4 != 0:
                    Player.y4 + 100
                elif Player.x4 < 1000 and Player.y4 == 700:
                    Player.x4 - 100
                elif Player.x4 == 0 and Player.y4 <= 700:
                    Player.y4 - 100
            elif "Seize any property" in chance_card:
                pass
            elif "snatches $200 from each player" in chance_card:
                pass
            elif "earthquake" in chance_card:
                pass
            Chance.chance_done = True


# settings for the property
price = 0
# price list is for player to buy property according to their price
Pricelist = [0, 500, 600, 700, 0, 2100, 800, 900, 1000, 0, 1200, 1300, 0, 1400, 1500, 1600,
             0, 1800, 1900, 2000, 0, 2150, 2200, 2400, 2500, 0, 2600, 2800, 0, 3000, 3500, 4000]
# List for property level
Property_level = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

name_list = ['Passngo', 'Ramly Burger', '99 Speedmarket', 'Aeon Big', 'tax', 'TNB', 'Batu Caves', 'Pulau Langkawi', 'Cameron Highland', 'parking', 'Gunung Mulu', 'Mount Kinabalu', 'chance', 'Johor Bahru', 'George Town',
             'Melaka', 'jail', 'KL Sentral', 'Port Dickson', 'MMU Cyberjaya', 'tax', 'Indah water', 'Genting Highland', 'Putrajaya', 'KLIA', 'injail', 'TRX', 'Pavilion KL', 'chance', 'KL Tower', 'Merdeka 118', 'KLCC']

b_property = str()
# Buying , rent price and upgrade price for all property
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
Property_with_rent = {
    'Ramly Burger': 10,
    '99 Speedmarket': 20,
    'Aeon Big': 35,
    'TNB': 40,
    'Batu Caves': 50,
    'Pulau Langkawi': 55,
    'Cameron Highland': 65,
    'Gunung Mulu': 80,
    'Mount Kinabalu': 85,
    'Johor Bahru': 100,
    'George Town': 110,
    'Melaka': 120,
    'KL Sentral': 140,
    'Port Dickson': 160,
    'MMU Cyberjaya': 160,
    'Indah water': 180,
    'Genting Highland': 180,
    'Putrajaya': 200,
    'KLIA': 220,
    'TRX': 230,
    'Pavilion KL': 240,
    'KL Tower': 275,
    'Merdeka 118': 350,
    'KLCC': 500
}
Property_upgrade_cost = {
    'Ramly Burger': 250,
    '99 Speedmarket': 300,
    'Aeon Big': 350,
    'TNB': 370,
    'Batu Caves': 400,
    'Pulau Langkawi': 450,
    'Cameron Highland': 500,
    'Gunung Mulu': 600,
    'Mount Kinabalu': 650,
    'Johor Bahru': 700,
    'George Town': 750,
    'Melaka': 800,
    'KL Sentral': 900,
    'Port Dickson': 950,
    'MMU Cyberjaya': 1000,
    'Genting Highland': 1100,
    'Putrajaya': 1200,
    'KLIA': 1250,
    'TRX': 1300,
    'Pavilion KL': 1400,
    'KL Tower': 1500,
    'Merdeka 118': 1750,
    'KLCC': 2000
}
# setting for player
initial_money = int(200)
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
# added a boolean condition to make the message only trigger one times
p1_broked = p2_broked = p3_broked = p4_broked = False


class economic:
    buy_clicked = False
    leco_dis1 = str()
    leco_dis2 = str()
    leco_dis3 = str()
    leco_dis4 = str()
    L_eco_dis1 = str()
    L_eco_dis2 = str()
    L_eco_dis3 = str()
    L_eco_dis4 = str()
    rent_display = str()
    rent_value = str()
    # checking for validity in buying property
    # player will not be able to click buy button if tile is not available to sell
    showing_pay_button = False

    # upgrade controlling bool
    showing_upgrade_button = False
    upgrading = False
    showing_buy_button = False
    # checking for price is 0 for validity of buying

    def check_buying_valid():
        if player_sequence == 1 and player1_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            if Pricelist[player1_pos] != 0:
                economic.showing_buy_button = True
            else:
                economic.showing_buy_button = False

        elif player_sequence == 2 and player2_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            if Pricelist[player2_pos] != 0:
                economic.showing_buy_button = True
            else:
                economic.showing_buy_button = False

        elif player_sequence == 3 and player3_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            if Pricelist[player3_pos] != 0:
                economic.showing_buy_button = True
            else:
                economic.showing_buy_button = False

        elif player_sequence == 4 and player4_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            if Pricelist[player4_pos] != 0:
                economic.showing_buy_button = True
            else:
                economic.showing_buy_button = False

        else:
            economic.showing_buy_button = False

    def buying_property():

        if player_sequence == 1 and player1_broke == False and not economic.buy_clicked:
            price = Pricelist[player1_pos]
            print(f"price ={price}")
            before_buy_p1 = player_dict_m['p1_money']
            player_dict_m['p1_money'] = before_buy_p1 - price
            after_buy_p1 = player_dict_m['p1_money']
            print(f'Player1 now have {after_buy_p1}$')
            economic.buy_clicked = True
            Button.is_buying_properties = True

        elif player_sequence == 2 and player2_broke == False and not economic.buy_clicked:
            price = Pricelist[player2_pos]
            print(f"price ={price}")
            before_buy_p2 = player_dict_m['p2_money']
            player_dict_m['p2_money'] = before_buy_p2 - price
            after_buy_p2 = player_dict_m['p2_money']
            print(f'Player2 now have {after_buy_p2}$')
            economic.buy_clicked = True
            Button.is_buying_properties = True

        elif player_sequence == 3 and player3_broke == False and not economic.buy_clicked:
            price = Pricelist[player3_pos]
            print(f"price ={price}")
            before_buy_p3 = player_dict_m['p3_money']
            player_dict_m['p3_money'] = before_buy_p3 - price
            after_buy_p3 = player_dict_m['p3_money']
            print(f'Player3 now have {after_buy_p3}$')
            economic.buy_clicked = True
            Button.is_buying_properties = True

        elif player_sequence == 4 and player4_broke == False and not economic.buy_clicked:
            price = Pricelist[player4_pos]
            print(f"price ={price}")
            before_buy_p4 = player_dict_m['p4_money']
            player_dict_m['p4_money'] = before_buy_p4 - price
            after_buy_p4 = player_dict_m['p4_money']
            print(f'Player4 now have {after_buy_p4}$')
            economic.buy_clicked = True
            Button.is_buying_properties = True

        else:
            price = 0
            pass
        Player.player_check_broke()
        economic.owning_property(price)

    def check_buy_button():
        if economic.showing_buy_button:
            if not Button.is_buying_properties:
                button_buy.update()

    def owning_property(price):
        middle = 0
        if player_sequence == 1 and Pricelist[player1_pos] != 0:
            b_property = [
                i for i in Property_with_price if Property_with_price[i] == price]
            b_property = ', '.join(b_property)
            p1_list_p.append(b_property)
            Display.activity = (f'P1 purchase {b_property} with {price}')
            if len(p1_list_p) >= 5:
                middle = len(p1_list_p)//2
                economic.leco_dis1 = p1_list_p[:middle]
                economic.L_eco_dis1 = p1_list_p[middle:]
                economic.leco_dis1 = (f'own {economic.leco_dis1}')
            else:
                economic.leco_dis1 = (f'own {p1_list_p}')
            Pricelist[player1_pos] = 0
        elif player_sequence == 2 and Pricelist[player2_pos] != 0:
            b_property = [
                i for i in Property_with_price if Property_with_price[i] == price]
            b_property = ', '.join(b_property)
            p2_list_p.append(b_property)
            Display.activity = (f'P2 purchase {b_property} with {price}')
            if len(p2_list_p) >= 5:
                middle = len(p2_list_p)//2
                economic.leco_dis2 = p2_list_p[:middle]
                economic.L_eco_dis2 = p2_list_p[middle:]
                economic.leco_dis2 = (f'own {economic.leco_dis2}')
            else:
                economic.leco_dis2 = (f'own {p2_list_p}')
            Pricelist[player2_pos] = 0
        elif player_sequence == 3 and Pricelist[player3_pos] != 0:
            b_property = [
                i for i in Property_with_price if Property_with_price[i] == price]
            b_property = ', '.join(b_property)
            p3_list_p.append(b_property)
            Display.activity = (f'P3 purchase {b_property} with {price}')
            if len(p3_list_p) >= 5:
                middle = len(p3_list_p)//2
                economic.leco_dis3 = p3_list_p[:middle]
                economic.L_eco_dis3 = p3_list_p[middle:]
                economic.leco_dis3 = (f'own {economic.leco_dis3}')
            else:
                economic.leco_dis3 = (f'own {p3_list_p}')
            Pricelist[player3_pos] = 0
        elif player_sequence == 4 and Pricelist[player4_pos] != 0:
            b_property = [
                i for i in Property_with_price if Property_with_price[i] == price]
            b_property = ', '.join(b_property)
            p4_list_p.append(b_property)
            Display.activity = (f'P4 purchase {b_property} with {price}')
            if len(p4_list_p) >= 5:
                middle = len(p4_list_p)//2
                economic.leco_dis4 = p4_list_p[:middle]
                economic.L_eco_dis4 = p4_list_p[middle:]
                economic.leco_dis4 = (f'own {economic.leco_dis4}')
            else:
                economic.leco_dis4 = (f'own {p4_list_p}')
            Pricelist[player4_pos] = 0

        else:
            pass


    def update_eco():
        global player_sequence
        title_font = pygame.font.Font("HelveticaNeue.ttf", 18)
        rent_font = pygame.font.Font("HelveticaNeue.ttf", 20)
        ldis_eco1 = economic.leco_dis1
        ldis_eco2 = economic.leco_dis2
        ldis_eco3 = economic.leco_dis3
        ldis_eco4 = economic.leco_dis4
        L_dis_eco1 = economic.L_eco_dis1
        L_dis_eco2 = economic.L_eco_dis2
        L_dis_eco3 = economic.L_eco_dis3
        L_dis_eco4 = economic.L_eco_dis4
        rent_display = economic.rent_display
        ldis_eco1 = title_font.render(f"{ldis_eco1}", True, black)
        L_dis_eco1 = title_font.render(f"{L_dis_eco1}", True, black)
        ldis_eco2 = title_font.render(f"{ldis_eco2}", True, black)
        L_dis_eco2 = title_font.render(f"{L_dis_eco2}", True, black)
        ldis_eco3 = title_font.render(f"{ldis_eco3}", True, black)
        L_dis_eco3 = title_font.render(f"{L_dis_eco3}", True, black)
        ldis_eco4 = title_font.render(f"{ldis_eco4}", True, black)
        L_dis_eco4 = title_font.render(f"{L_dis_eco4}", True, black)
        rent_display = rent_font.render(f"{rent_display}", True, black)
        # showing player current activity
        if player_sequence == 1 and not paying:
            screen.blit(ldis_eco1, (120, 140))
            screen.blit(L_dis_eco1, (120, 160))
        elif player_sequence == 2 and not paying:
            screen.blit(ldis_eco2, (120, 140))
            screen.blit(L_dis_eco2, (120, 160))
        elif player_sequence == 3 and not paying:
            screen.blit(ldis_eco3, (120, 140))
            screen.blit(L_dis_eco3, (120, 160))
        elif player_sequence == 4 and not paying:
            screen.blit(ldis_eco4, (120, 140))
            screen.blit(L_dis_eco4, (120, 160))
        elif player_sequence != 0 and paying:
            screen.blit(rent_display, (100, 140))

    def checking_rent_valid():
        global paying
        if player_sequence == 1 and Pricelist[player1_pos] != 0:
            pass
        if player_sequence == 2 and Pricelist[player2_pos] != 0:
            pass
        if player_sequence == 3 and Pricelist[player3_pos] != 0:
            pass
        if player_sequence == 4 and Pricelist[player4_pos] != 0:
            pass
        else:
            # player not landed in any of the buyable or unown property
            # checking for rent
            economic.paying_for_rent()

    def paying_for_rent():
        global paying
        # check if player 1 needed to pay another player rent
        if player_sequence == 1 and player1_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            property_rent = name_list[player1_pos]
            rent_price = Property_with_rent[property_rent]
            rent_in_list = (
                property_rent in p2_list_p or property_rent in p3_list_p or property_rent in p4_list_p)
            if rent_in_list:
                if property_rent in p2_list_p:
                    economic.rent_display = (
                        f"Player {player_sequence} paying {rent_price} for {property_rent} of player 2 rent")
                elif property_rent in p3_list_p:
                    economic.rent_display = (
                        f"Player {player_sequence} paying {rent_price} for {property_rent} of player 3 rent")
                elif property_rent in p4_list_p:
                    economic.rent_display = (
                        f"Player {player_sequence} paying {rent_price} for {property_rent} of player 4 rent")
                paying = True

        if player_sequence == 2 and player2_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:

            property_rent = name_list[player2_pos]
            rent_price = Property_with_rent[property_rent]
            rent_in_list = (
                property_rent in p1_list_p or property_rent in p3_list_p or property_rent in p4_list_p)
            if rent_in_list:
                if property_rent in p1_list_p:
                    economic.rent_display = (
                        f"Player {player_sequence} paying {rent_price} for {property_rent} of player 1 rent")
                elif property_rent in p3_list_p:
                    economic.rent_display = (
                        f"Player {player_sequence} paying {rent_price} for {property_rent} of player 3 rent")
                elif property_rent in p4_list_p:
                    economic.rent_display = (
                        f"Player {player_sequence} paying {rent_price} for {property_rent} of player 4 rent")
                paying = True

        if player_sequence == 3 and player3_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            property_rent = name_list[player3_pos]
            rent_price = Property_with_rent[property_rent]
            rent_in_list = (
                property_rent in p1_list_p or property_rent in p2_list_p or property_rent in p4_list_p)
            if rent_in_list:
                if property_rent in p1_list_p:
                    economic.rent_display = (
                        f"Player {player_sequence} paying {rent_price} for {property_rent} of player 1 rent")
                elif property_rent in p2_list_p:
                    economic.rent_display = (
                        f"Player {player_sequence} paying {rent_price} for {property_rent} of player 2 rent")
                elif property_rent in p4_list_p:
                    economic.rent_display = (
                        f"Player {player_sequence} paying {rent_price} for {property_rent} of player 4 rent")
                paying = True
        if player_sequence == 4 and player4_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:

            property_rent = name_list[player4_pos]
            rent_price = Property_with_rent[property_rent]
            rent_in_list = (
                property_rent in p1_list_p or property_rent in p3_list_p or property_rent in p2_list_p)
            if rent_in_list:
                if property_rent in p1_list_p:
                    economic.rent_display = (
                        f"Player {player_sequence} paying {rent_price} for {property_rent} of player 1 rent")
                elif property_rent in p2_list_p:
                    economic.rent_display = (
                        f"Player {player_sequence} paying {rent_price} for {property_rent} of player 2 rent")
                elif property_rent in p3_list_p:
                    economic.rent_display = (
                        f"Player {player_sequence} paying {rent_price} for {property_rent} of player 3 rent")
                paying = True

    def rent_button_1():
        global paying
        if player_sequence == 1 and player1_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            property_rent = name_list[player1_pos]
            # checking for a property is not own by player 1
            if property_rent in p2_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 2")
                print(f"Player 1 paying {rent_price} for player 2")
                Display.activity = (f"Player 1 paying {
                                    rent_price} for player 2")
                player_dict_m['p1_money'] -= rent_price
                player_dict_m['p2_money'] += rent_price
                print(f"Player 1 now have {player_dict_m['p1_money']}")
                print(f"Player 2 now have {player_dict_m['p2_money']}")
                paying = False

            if property_rent in p3_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 3")
                print(f"Player 1 paying {rent_price} for player 3")
                Display.activity = (f"Player 1 paying {
                                    rent_price} for player 3")
                player_dict_m['p1_money'] -= rent_price
                player_dict_m['p3_money'] += rent_price
                print(f"Player 1 now have {player_dict_m['p1_money']}")
                print(f"Player 3 now have {player_dict_m['p3_money']}")
                paying = False

            if property_rent in p4_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 4")
                print(f"Player 1 paying {rent_price} for player 4")
                Display.activity = (f"Player 1 paying {
                                    rent_price} for player 4")
                player_dict_m['p1_money'] -= rent_price
                player_dict_m['p4_money'] += rent_price
                print(f"Player 1 now have {player_dict_m['p1_money']}")
                print(f"Player 4 now have {player_dict_m['p4_money']}")
                paying = False

            else:
                paying == False
            Player.player_check_broke()

    def rent_button_2():
        global paying
        if player_sequence == 2 and player2_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            property_rent = name_list[player2_pos]
            # checking for a property is not own by player 2
            if property_rent in p1_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 1")
                print(f"Player 2 paying {rent_price} for player 1")
                Display.activity = (f"Player 2 paying {
                                    rent_price} for player 1")
                player_dict_m['p2_money'] -= rent_price
                player_dict_m['p1_money'] += rent_price
                print(f"Player 2 now have {player_dict_m['p2_money']}")
                print(f"Player 1 now have {player_dict_m['p1_money']}")
                paying = False
            if property_rent in p3_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 3")
                print(f"Player 2 paying {rent_price} for player 3")
                Display.activity = (f"Player 2 paying {
                                    rent_price} for player 3")
                player_dict_m['p2_money'] -= rent_price
                player_dict_m['p3_money'] += rent_price
                print(f"Player 2 now have {player_dict_m['p2_money']}")
                print(f"Player 2 now have {player_dict_m['p2_money']}")
                paying = False
            if property_rent in p4_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 4")
                print(f"Player 2 paying {rent_price} for player 4")
                Display.activity = (f"Player 2 paying {
                                    rent_price} for player 4")
                player_dict_m['p2_money'] -= rent_price
                player_dict_m['p4_money'] += rent_price
                print(f"Player 2 now have {player_dict_m['p2_money']}")
                print(f"Player 4 now have {player_dict_m['p4_money']}")
                paying = False
            else:
                pass
            Player.player_check_broke()

    def rent_button_3():
        global paying
        if player_sequence == 3 and player3_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            property_rent = name_list[player3_pos]
            # checking for a property is not own by player 3
            if property_rent in p1_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 1")
                print(f"Player 3 paying {rent_price} for player 1")
                Display.activity = (f"Player 3 paying {
                                    rent_price} for player 1")
                player_dict_m['p3_money'] -= rent_price
                player_dict_m['p1_money'] += rent_price
                print(f"Player 3 now have {player_dict_m['p3_money']}")
                print(f"Player 1 now have {player_dict_m['p1_money']}")
                paying = False
            if property_rent in p2_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 2")
                print(f"Player 3 paying {rent_price} for player 2")
                Display.activity = (f"Player 3 paying {
                                    rent_price} for player 2")
                player_dict_m['p3_money'] -= rent_price
                player_dict_m['p2_money'] += rent_price
                print(f"Player 3 now have {player_dict_m['p3_money']}")
                print(f"Player 2 now have {player_dict_m['p2_money']}")
                paying = False
            if property_rent in p4_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 4")
                print(f"Player 3 paying {rent_price} for player 4")
                Display.activity = (f"Player 3 paying {
                                    rent_price} for player 4")
                player_dict_m['p3_money'] -= rent_price
                player_dict_m['p4_money'] += rent_price
                print(f"Player 3 now have {player_dict_m['p3_money']}")
                print(f"Player 4 now have {player_dict_m['p4_money']}")
                paying = False
            else:
                pass
            Player.player_check_broke()

    def rent_button_4():
        global paying
        if player_sequence == 4 and player4_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            property_rent = name_list[player4_pos]
            # checking for a property is not own by player 4
            if property_rent in p1_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 1")
                print(f"Player 4 paying {rent_price} for player 1")
                Display.activity = (f"Player 4 paying {
                                    rent_price} for player 1")
                player_dict_m['p4_money'] -= rent_price
                player_dict_m['p1_money'] += rent_price
                print(f"Player 4 now have {player_dict_m['p4_money']}")
                print(f"Player 1 now have {player_dict_m['p1_money']}")
                paying = False

            if property_rent in p2_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 2")
                print(f"Player 4 paying {rent_price} for player 2")
                Display.activity = (f"Player 4 paying {
                                    rent_price} for player 2")
                player_dict_m['p4_money'] -= rent_price
                player_dict_m['p2_money'] += rent_price
                print(f"Player 4 now have {player_dict_m['p4_money']}")
                print(f"Player 2 now have {player_dict_m['p2_money']}")
                paying = False

            if property_rent in p3_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 3")
                print(f"Player 4 paying {rent_price} for player 3")
                Display.activity = (f"Player 4 paying {
                                    rent_price} for player 3")
                player_dict_m['p4_money'] -= rent_price
                player_dict_m['p3_money'] += rent_price
                print(f"Player 4 now have {player_dict_m['p4_money']}")
                print(f"Player 3 now have {player_dict_m['p3_money']}")
                paying = False
            else:
                pass
            Player.player_check_broke()

    def check_upgrade():
        if player_sequence == 1 and player1_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            if Pricelist[player1_pos] == 0 and name_list[player1_pos] in p1_list_p:
                economic.showing_upgrade_button = True
            else:
                economic.showing_upgrade_button = False

        elif player_sequence == 2 and player2_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            if Pricelist[player2_pos] == 0 and name_list[player2_pos] in p2_list_p:
                economic.showing_upgrade_button = True
            else:
                economic.showing_upgrade_button = False

        elif player_sequence == 3 and player3_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            if Pricelist[player3_pos] == 0 and name_list[player3_pos] in p3_list_p:
                economic.showing_upgrade_button = True
            else:
                economic.showing_upgrade_button = False

        elif player_sequence == 4 and player4_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            if Pricelist[player4_pos] == 0 and name_list[player4_pos] in p4_list_p:
                economic.showing_upgrade_button = True
            else:
                economic.showing_upgrade_button = False

    def check_upgrade_button():
        if economic.showing_upgrade_button:
            if not economic.upgrading:
                button_upgrade.update()

    def upgrade_player1():
        property_level = Property_level[player1_pos]
        upgrading_property = name_list[player1_pos]
        before_upgrade_rent = Property_with_rent[upgrading_property]
        upgrade_price = Property_upgrade_cost[upgrading_property]

        # if the player has'nt reach maximum level
        if property_level <= 3 and economic.upgrading and economic.showing_upgrade_button:
            Property_level[player1_pos] += 1
            print(f'Player 1 is upgrading {
                upgrading_property} with {upgrade_price}')
            player_dict_m["p1_money"] -= upgrade_price
            after_upgrade_rent = before_upgrade_rent * 1.5
            print(f'the property level is now{Property_level[player1_pos]}')
            print(f'new rent price is {after_upgrade_rent}')
            Display.activity = (f'P1 upgrade {upgrading_property} into level{
                                property_level} with {upgrade_price}')
            Property_with_rent[upgrading_property] = after_upgrade_rent
            economic.showing_upgrade_button = False
            # if the player has reach maximum level
        if property_level == 3 and economic.upgrading and economic.showing_upgrade_button:
            Property_level[player1_pos] += 1
            print(f'Player 1 is upgrading {
                upgrading_property} with {upgrade_price}')
            player_dict_m["p1_money"] -= upgrade_price
            print(f'the property level is now{
                  Property_level[player1_pos]} and has reach the maximum level')
            after_upgrade_rent = before_upgrade_rent * 2
            print(f'new rent price is {after_upgrade_rent}')
            Property_with_rent[upgrading_property] = after_upgrade_rent
            economic.showing_upgrade_button = False
        elif property_level > 4:
            print(f'{upgrading_property} have reach the highest level')
            economic.showing_upgrade_button = False

    def upgrade_player2():
        property_level = Property_level[player2_pos]
        upgrading_property = name_list[player2_pos]
        before_upgrade_rent = Property_with_rent[upgrading_property]
        upgrade_price = Property_upgrade_cost[upgrading_property]

        # if the player has'nt reach maximum level
        if property_level <= 3 and economic.upgrading and economic.showing_upgrade_button:
            Property_level[player2_pos] += 1
            print(f'Player 2 is upgrading {
                upgrading_property} with {upgrade_price}')
            player_dict_m["p2_money"] -= upgrade_price
            after_upgrade_rent = before_upgrade_rent * 1.5
            print(f'the property level is now{Property_level[player2_pos]}')
            print(f'new rent price is {after_upgrade_rent}')
            Display.activity = (f'P2 upgrade {upgrading_property} into level{
                                property_level} with {upgrade_price}')
            Property_with_rent[upgrading_property] = after_upgrade_rent
            economic.showing_upgrade_button = False
            # if the player has reach maximum level
        if property_level == 3 and economic.upgrading and economic.showing_upgrade_button:
            Property_level[player2_pos] += 1
            print(f'Player 2 is upgrading {
                upgrading_property} with {upgrade_price}')
            player_dict_m["p2_money"] -= upgrade_price
            print(f'the property level is now{
                  Property_level[player2_pos]} and has reach the maximum level')
            after_upgrade_rent = before_upgrade_rent * 2
            print(f'new rent price is {after_upgrade_rent}')
            Property_with_rent[upgrading_property] = after_upgrade_rent
            economic.showing_upgrade_button = False

        elif property_level > 4:
            print(f'{upgrading_property} have reach the highest level')
            economic.showing_upgrade_button = False

    def upgrade_player3():
        property_level = Property_level[player3_pos]
        upgrading_property = name_list[player3_pos]
        before_upgrade_rent = Property_with_rent[upgrading_property]
        upgrade_price = Property_upgrade_cost[upgrading_property]

        # if the player has'nt reach maximum level
        if property_level <= 3 and economic.upgrading and economic.showing_upgrade_button:
            Property_level[player3_pos] += 1
            print(f'Player 3 is upgrading {upgrading_property} with {upgrade_price}')
            player_dict_m["p3_money"] -= upgrade_price
            after_upgrade_rent = before_upgrade_rent * 1.5
            print(f'the property level is now{Property_level[player3_pos]}')
            print(f'new rent price is {after_upgrade_rent}')
            Display.activity = (f'P3 upgrade {upgrading_property} into level{
                                property_level} with {upgrade_price}')
            Property_with_rent[upgrading_property] = after_upgrade_rent
            economic.showing_upgrade_button = False
            # if the player has reach maximum level
        if property_level == 3 and economic.upgrading and economic.showing_upgrade_button:
            Property_level[player3_pos] += 1
            print(f'Player 3 is upgrading {upgrading_property} with {upgrade_price}')
            player_dict_m["p3_money"] -= upgrade_price
            print(f'the property level is now{Property_level[player3_pos]} and has reach the maximum level')
            after_upgrade_rent = before_upgrade_rent * 2
            print(f'new rent price is {after_upgrade_rent}')
            Property_with_rent[upgrading_property] = after_upgrade_rent
            economic.showing_upgrade_button = False
        elif property_level > 4:
            print(f'{upgrading_property} have reach the highest level')
            economic.showing_upgrade_button = False

    def upgrade_player4():
        property_level = Property_level[player4_pos]
        upgrading_property = name_list[player4_pos]
        before_upgrade_rent = Property_with_rent[upgrading_property]
        upgrade_price = Property_upgrade_cost[upgrading_property]

        # if the player has'nt reach maximum level
        if property_level <= 3 and economic.upgrading and economic.showing_upgrade_button:
            Property_level[player4_pos] += 1
            print(f'Player 4 is upgrading {
                upgrading_property} with {upgrade_price}')
            player_dict_m["p4_money"] -= upgrade_price
            after_upgrade_rent = before_upgrade_rent * 1.5
            print(f'the property level is now{Property_level[player3_pos]}')
            print(f'new rent price is {after_upgrade_rent}')
            Display.activity = (f'P1 upgrade {upgrading_property} into level{
                                property_level} with {upgrade_price}')
            Property_with_rent[upgrading_property] = after_upgrade_rent
            economic.showing_upgrade_button = False
            # if the player has reach maximum level
        if property_level == 3 and economic.upgrading and economic.showing_upgrade_button:
            Property_level[player4_pos] += 1
            print(f'Player 4 is upgrading {
                upgrading_property} with {upgrade_price}')
            player_dict_m["p4_money"] -= upgrade_price
            print(f'the property level is now{
                  Property_level[player4_pos]} and has reach the maximum level')
            after_upgrade_rent = before_upgrade_rent * 2
            print(f'new rent price is {after_upgrade_rent}')
            Property_with_rent[upgrading_property] = after_upgrade_rent
            economic.showing_upgrade_button = False
        elif property_level > 4:
            print(f'{upgrading_property} have reach the highest level')
            economic.showing_upgrade_button = False

    def tax():
        if player_sequence == 1:
            print('player1 paying tax')
            Display.activity = (f'Player 1 is paying 1500 tax')
            player_dict_m['p1_money'] -= 1500
        if player_sequence == 2:
            print('player2 paying tax')
            Display.activity = (f'Player 2 is paying 1500 tax')
            player_dict_m["p2_money"] -= 1500
        if player_sequence == 3:
            print('player3 paying tax')
            Display.activity = (f'Player 3 is paying 1500 tax')
            player_dict_m["p3_money"] -= 1500
        if player_sequence == 4:
            print('player4 paying tax')
            Display.activity = (f'Player 4 is paying 1500 tax')
            player_dict_m["p4_money"] -= 1500
        Player.player_check_broke()


class starting_menu:
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    speed = 3
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
    rules_2 = "Game is played by 2-4 players"
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

mouse_click = pygame.mixer.Sound('Sound/mouse_click1.mp3')

button_functions = [button_music.checkmusic, button_roll.checkroll, button_pay.check_pay, button_chance.check_chance,
                    button_play.check_play, button_buy.check_buy, button_next.checkload_finish, button_exit.check_exit, button_upgrade.check_upgrade, button_2p.player_num_2, button_3p.player_num_3, button_4p.player_num_4]


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


def disaster_eartquake():
    # adjusting another value after 1 can change it's possibilities
    possibilities = random.randint(1, 80)
    if round_num >= 1:
        if possibilities == 1:
            print("oh no a earthquake happen")
            print('player 1 donate 500')
            player_dict_m['p1_money'] -= 500
        if possibilities == 2:
            print("oh no a earthquake happen")
            print('player 2 donate 500')
            player_dict_m['p2_money'] -= 500
        if possibilities == 3:
            print("oh no a earthquake happen")
            print('player 3 donate 500')
            player_dict_m['p3_money'] -= 500
        if possibilities == 4:
            print("oh no a earthquake happen")
            print('player 4 donate 500')
            player_dict_m['p4_money'] -= 500
        Player.player_check_broke()


def disaster_tornado():
    possibilities = random.randint(1, 100)
    if round_num >= 1:
        if possibilities == 1:
            print("oh no a tornoda hit player 1")
            print('player 1 loss 1000')
            player_dict_m['p1_money'] -= 1000
        if possibilities == 2:
            print("oh no a tornado hit player 2")
            print('player 2 loss 1000')
            player_dict_m['p2_money'] -= 1000
        if possibilities == 3:
            print("oh no a tornado hit player 3")
            print('player 3 donate 1000')
            player_dict_m['p3_money'] -= 1000
        if possibilities == 4:
            print("oh no a tornado happen")
            print('player 4 donate 1000')
            player_dict_m['p4_money'] -= 1000
        Player.player_check_broke()


# variable to control and skip player

player_num2 = False
player_num3 = False


def skipping_player():
    global player_sequence
    if player_num2:
        if player_sequence == 2:
            player_sequence += 1
        if player_sequence == 3:
            player_sequence += 1

    elif player_num3:
        if player_sequence == 3:
            player_sequence += 1
    if player1_broke:
        if player_sequence == 0:
            player_sequence += 1
    if player2_broke:
        if player_sequence == 1:
            player_sequence += 1
    if player3_broke:
        if player_sequence == 2:
            player_sequence += 1
    if player4_broke:
        if player_sequence == 3:
            player_sequence += 1


def choose_player_num():
    screen.blit(Display.players_num_image, Display.players_num_image_rect)
    button_2p.update()
    button_3p.update()
    button_4p.update()


run = True

# main loop for python
while run:
    clock.tick(fps)
    screen.fill((0, 0, 0))

    if Button.exit_game and Button.menu:
        run = False

    if Button.menu:
        button_play.update()
        button_exit.update()
        starting_menu.title()

    if not Button.menu and Button.loading:
        button_next.update()
        starting_menu.loading_screen()
        starting_menu.showing_rule()

    if not Display.show_loading_done and not Button.loading:
        pass
        # remember change show_loading_done back to false when activate this def
        Display.show_player_explain()
    if Display.show_loading_done and not Button.player_choose:
        choose_player_num()

    if Button.player_choose:
        map.draw()
        Display.middle()
        Display.showing_dim_button()
        Display.showing_player_round()
        Display.showing_player_money()
        Display.showing_activity()
        Display.showing_properties_name()
        economic.update_eco()
        button_music.update()
        Chance.check_chance_valid()
        button_roll.update()
        Player.show_players()
        moving_sprites.draw(screen)
        moving_sprites.update()
        economic.check_buying_valid()
        economic.check_buy_button()
        economic.check_upgrade_button()

        if paying:
            button_pay.update()
        if Chance.showing_chance:
            button_chance.update()
        economic.check_buying_valid()
        Player.show_players()
        moving_sprites.draw(screen)
        moving_sprites.update()
        if paying:
            button_pay.update()

        if show_description and time.time() - description_display_timer < description_display_duration:
            display_descriptions(description)
        else:
            show_description = False

        # Display.drawing_grid(100)
    else:
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_click.play()
            handle_button_events(pygame.mouse.get_pos())
            display_description_block(pygame.mouse.get_pos())
            
        # if roll dice randomize a num
            if Button.rolling_con and Display.show_loading_done:
                Dice.rand_a_dice()
                if not paying:
                    skipping_player()
                    # disaster_eartquake()
                    # disaster_tornado()
                    dice_num = (random.randint(1, 6))
                    Player.player_movement(dice_num)
                    Player.move(dice_num)
                    Player.player_check_win()
                    economic.upgrading = False
                    economic.buy_clicked = False
                    Button.is_buying_properties = False

                if not changing_round and not paying:
                    # dice animating preventing player move again when changing round
                    dice.animate(dice_num)
                    Button.rolling_con = False
                    buy_clicked = False
                    economic.checking_rent_valid()
                    economic.check_upgrade()

            else:
                pass

    pygame.display.update()
pygame.quit()