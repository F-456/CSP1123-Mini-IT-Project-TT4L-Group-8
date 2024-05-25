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
    4: "'Aeon Big' is a supermarket. When ur state got the aeon supermarket, ur state will be certified as 'developed state'.(JKJK)",
    6: "'Tenaga National Berhad(TNB)', is the Malaysian multinational electricity company and is the only electric utility company in Peninsular Malaysia and also the largest publicly listed power company in Southeast Asia with MYR 182.60 billion worth of assets.",
    7: "'Batu Caves' is a mogote (a type of karst landform) that has a series of caves and cave temples in Gombak, Selangor, Malaysia. The cave complex is one of the most popular Hindu shrines outside India, and is dedicated to Murugan. It is the focal point of the Tamil festival of Thaipusam in Malaysia.",
    8: "'Pulau Langkawi' is a duty-free island and an archipelago of 99 islands located some 30 km off the coast of northwestern Malaysia and a few kilometres south of Ko Tarutao, adjacent to the Thai border.",
    9: "'Cameroon Highland'is a district in Pahang, Malaysia, occupying an area of 712.18 square kilometres. Developed in the 1930s, the tableland is one of the oldest tourist spots in Malaysia.",
    11: "'Gunung Mulu National Park' is in Miri Division, Sarawak, Malaysia. It is a UNESCO World Heritage Site that encompasses caves and karst formations in a mountainous equatorial rainforest setting",
    12: "'Mount Kinabalu' is the highest mountain in Borneo and Malaysia. With an elevation of 4,095 metres (13,435 ft), it is the third-highest peak of an island on Earth, the 28th highest peak in Southeast Asia, and 20th most prominent mountain in the world.",
    14: "'Johor Bahru' colloquially referred to as JB, and the capital city of the state of Johor, Malaysia (the second-largest district in the country, by population). It is the second-largest national GDP-contributor among the major cities in Malaysia, and forms a part of Iskandar Malaysia, the nation's largest special economic zone, by investment value.",
    15: "'George Town' is the capital of the Malaysian state of Penang. Malaysia's second largest metropolitan area with a population of 2.84 million and the second highest contributor to the country's GDP. The city proper spans an area of 306 km2 (118 sq mi) encompassing Penang Island and surrounding islets.",
    16: "'Malacca (Malay: Melaka)', officially the Historic State of Malacca, is a state in Malaysia located in the southern region of the Malay Peninsula, facing the Strait of Malacca. Its capital is Malacca City, which has been listed as a UNESCO World Heritage Site since 7 July 2008.",
    18: "'Kuala Lumpur Sentral Station (KL Sentral)' is a transit-oriented development that houses the main railway station of Kuala Lumpur, the capital of Malaysia. Opened on 16 April 2001, KL Sentral replaced the old Kuala Lumpur railway station as the city's main intercity railway station. KL Sentral is the largest railway station in Malaysia, and also in Southeast Asia from 2001 to 2021",
    19: "'Port Dickson' colloquially referred to as PD is a beach resort in Port Dickson District, Negeri Sembilan, Malaysia. It is the second largest urban area in Negeri Sembilan after Seremban, its state capital.",
    20: "'MMU Cyberjaya' GOAT!! The BEST university you can find in MALAYSIA, the lecturers are also the best, especially MR Willie Poh.(PLS rate excellent for us)",
    22: "'Indah Water Konsortium Sdn. Bhd' is a Malaysian national wastewater and sanitation company, It is a government-owned company under the Minister of Finance Incorporated, which has the task of developing and maintaining a modern and efficient sewerage system for West Malaysia",
    23: "'Genting Highlands' is a hill station located in the state of Pahang, at 1800 metres elevation. It was established in 1965 by the late Malaysian businessman Lim Goh Tong. The primary tourist attraction is Resorts World Genting, a hill resort where casinos and theme parks are situated and where gambling is permitted. Many of Pahang's skyscrapers can be found here.",
    24: "'Putrajaya' is the administrative centre of Malaysia. The seat of the federal government of Malaysia was moved in 1999 from Kuala Lumpur to Putrajaya because of overcrowding and congestion in Kuala Lumpur, whilst the seat of the judiciary of Malaysia was later moved to Putrajaya in 2003",
    25: "'Kuala Lumpur International Airport (KLIA)' is the main international airport serving Kuala Lumpur, the capital of Malaysia. It is located in the Sepang District of Selangor. KLIA is the largest and busiest airport in Malaysia. In 2023, it handled 47,224,000 passengers, 660,040 tonnes of cargo and 319,026 aircraft movements. It is the world's 35th-busiest airport by total passenger traffic.",
    27: "'Tun Razak Exchange(TRX)' is a 70-acre development by Ministry of Finance Malaysia (MOF) in the heart of Kuala Lumpur for international finance and business. The development was named the second Prime Minister of Malaysia, Tun Abdul Razak Hussein. TRX is a strategic enabler of the Malaysian government's Economic Transformation Programme (ETP).",
    28: "'Pavilion, KL' is a premier shopping destination in the heart of Bukit Bintang, Malaysia. It offers luxury retail, diverse dining options, and stunning architecture highlighted by the iconic Crystal Fountain. ",
    30: "'The Kuala Lumpur Tower(KL Tower)' is a 6-storey, 421-metre-tall (1,381 ft) telecommunication tower in Kuala Lumpur, Malaysia. It is the world's seventh-tallest tower. The rest of the tower below has a stairwell and an elevator to reach the upper area, which also contains a revolving restaurant, providing diners with a panoramic view of the city.",
    31: "'Merdeka 118' is a 118-story megatall skyscraper in Kuala Lumpur, Malaysia. At 678.9 m (2,227 ft) tall, it is the second-tallest building and structure in the world, only behind the Burj Khalifa at 828 m (2,717 ft).",
    32: "'Petronas Twin Towers or KLCC Twin Towers' are an interlinked pair of 88-story supertall skyscrapers in Kuala Lumpur, Malaysia, standing at 451.9 metres (1,483 feet). From 1998 to 2004, they were officially designated as the tallest buildings in the world until completion of the Taipei 101, tallest twin skyscrapers and remained the tallest buildings in Malaysia until 2019."
}


def display_descriptions(description):
    max_width = 500
    max_height = 400

    # Create a surface to render text
    description_surface = pygame.Surface((max_width, max_height))
    description_surface.fill(grey)

    font = pygame.font.Font("HelveticaNeue.ttf", 24)
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
    current_money_d = int()
    current_round = str()
    # displaying image

    show_players_image = pygame.transform.scale(pygame.image.load(
        'pic/loading background.png').convert_alpha(), (1000, 800))
    show_players_image_rect = show_players_image.get_rect(
        center=(screen_width//2, screen_height//2))
    show_load_bool = True
    limit = 0
    alpha = 0
    show_loading_done = False
    # adding a boolean to control the function to loop one times

    def show_loading():
        # adding a limit to control when the if expression end
        Display.limit += 1
        if Display.show_load_bool and Display.alpha <= 255:
            # adjusting the value to adjust the appear speed
            Display.alpha += 0.9
            if Display.limit >= 450 or Display.alpha >= 255:
                Display.show_load_bool = False
        if not Display.show_load_bool:
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

    def showing_player_money():
        text_font = pygame.font.Font("HelveticaNeue.ttf", 22)
        if player_sequence == 0:
            Display.current_round = round_num
        if player_sequence == 1:
            Display.current_money_d = player_dict_m['p1_money']
        elif player_sequence == 2:
            Display.current_money_d = player_dict_m['p2_money']
        elif player_sequence == 3:
            Display.current_money_d = player_dict_m['p3_money']
        elif player_sequence == 4:
            Display.current_money_d = player_dict_m['p4_money']
        if player_sequence != 0:
            current_player = text_font.render(
                f"Player {player_sequence} now have {Display.current_money_d}", True, (black))
            screen.blit(current_player, (100, 110))
            # showing which round of current when player sequence is 0
        elif player_sequence == 0:
            current_player = text_font.render(
                f"Current round = {Display.current_round}", True, (black))
            screen.blit(current_player, (100, 110))

    def showing_dim_button():
        button_pay_dim.update()
        button_buy_dim.update()


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
    exit_game = False
    loading = True
    rolling_con = False
    is_buying_properties = False
    is_paying_rent = False

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
            economic.showing_pay_button = True

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
# adjust size
button_surface_on = pygame.transform.scale(button_surface_on, (40, 40))
button_surface_off = pygame.transform.scale(button_surface_off, (40, 40))
button_roll = pygame.transform.scale(button_roll, (80, 80))
button_play = pygame.transform.scale(button_play, (240, 150))
button_pay = pygame.transform.scale(button_pay, (120, 80))
button_pay_dim = pygame.transform.scale(button_pay_dim, (120, 80))
button_exit = pygame.transform.scale(button_exit, (240, 150))
button_next = pygame.transform.scale(button_next, (120, 100))
button_buy = pygame.transform.scale(button_buy, (120, 100))
button_buy_dim = pygame.transform.scale(button_buy_dim, (120, 100))
# adjust location
button_music = Button(button_surface_on, button_surface_off, 880, 120)
button_roll = Button(button_roll, button_roll, 800, 650)
button_play = Button(button_play, button_play, 700, 600)
button_exit = Button(button_exit, button_exit, 300, 600)
button_next = Button(button_next, button_next, 800, 600)
button_buy = Button(button_buy, button_buy, 800, 550)
button_buy_dim = Button(button_buy_dim, button_buy_dim, 800, 550)
button_pay = Button(button_pay, button_pay, 650, 560)
button_pay_dim = Button(button_pay_dim, button_pay_dim, 650, 560)

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


go_position = (0, 0)  # position for "GO"
bramly_position = (2, 1)  # position for "B.Ramly"
free_parking_position = (9, 1)  # position for Free Parking
jail_position = (1, 8)  # position for Jail


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
dice = Dice(750, 350)
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
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    x3 = 0
    y3 = 0
    x4 = 0
    y4 = 0

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
        if player_sequence == 1 and Player.x1 < 1000 and Player.y1 == 0:
            Player.x1 += step * 100
            # check if player exceed x boundary and needed to turn down
            if Player.x1 >= 1000:
                second_step = Player.x1 - 1000
                Player.x1 = 900
                Player.y1 += second_step + 100

        elif player_sequence == 1 and Player.x1 == 900 and Player.y1 != 0:
            Player.y1 += step * 100
            if Player.y1 >= 800:
                second_step = Player.y1 - 800
                Player.y1 = 700
                Player.x1 -= second_step
                Player.x1 -= 100

        elif player_sequence == 1 and Player.x1 < 1000 and Player.y1 == 700:
            Player.x1 -= step * 100
            if Player.x1 <= 0:
                second_step = 0 - Player.x1
                Player.x1 = 0
                Player.y1 = 700 - second_step

        elif player_sequence == 1 and Player.x1 == 0 and Player.y1 <= 700:
            Player.y1 -= step * 100
            if Player.y1 <= 0:
                second_step = 0 - Player.y1
                Player.y1 = 0
                Player.x1 = second_step

        if player_sequence == 2 and Player.x2 < 1000 and Player.y2 == 0:
            Player.x2 += step * 100
            if Player.x2 >= 1000:
                second_step = Player.x2 - 1000
                Player.x2 = 900
                Player.y2 += second_step + 100

        elif player_sequence == 2 and Player.x2 == 900 and Player.y2 != 0:
            Player.y2 += step * 100
            if Player.y2 >= 800:
                second_step = Player.y2 - 800
                Player.y2 = 700
                Player.x2 -= second_step
                Player.x2 -= 100

        elif player_sequence == 2 and Player.x2 < 1000 and Player.y2 == 700:
            Player.x2 -= step * 100
            if Player.x2 <= 0:
                second_step = 0 - Player.x2
                Player.x2 = 0
                Player.y2 = 700 - second_step

        elif player_sequence == 2 and Player.x2 == 0 and Player.y2 <= 700:
            Player.y2 -= step * 100
            if Player.y2 <= 0:
                second_step = 0 - Player.y2
                Player.y2 = 0
                Player.x2 = second_step

        if player_sequence == 3 and Player.x3 < 1000 and Player.y3 == 0:
            Player.x3 += step * 100
            if Player.x3 >= 1000:
                second_step = Player.x3 - 1000
                Player.x3 = 900
                Player.y3 += second_step + 100

        elif player_sequence == 3 and Player.x3 == 900 and Player.y3 != 0:
            Player.y3 += step * 100
            if Player.y3 >= 800:
                second_step = Player.y3 - 800
                Player.y3 = 700
                Player.x3 -= second_step
                Player.x3 -= 100

        elif player_sequence == 3 and Player.x3 < 1000 and Player.y3 == 700:
            Player.x3 -= step * 100
            if Player.x3 <= 0:
                second_step = 0 - Player.x3
                Player.x3 = 0
                Player.y3 = 700 - second_step

        elif player_sequence == 3 and Player.x3 == 0 and Player.y3 <= 700:
            Player.y3 -= step * 100
            if Player.y3 <= 0:
                second_step = 0 - Player.y3
                Player.y3 = 0
                Player.x3 = second_step

        if player_sequence == 4 and Player.x4 < 1000 and Player.y4 == 0:
            Player.x4 += step * 100
            if Player.x4 >= 1000:
                second_step = Player.x4 - 1000
                Player.x4 = 900
                Player.y4 += second_step + 100

        elif player_sequence == 4 and Player.x4 == 900 and Player.y4 != 0:
            Player.y4 += step * 100
            if Player.y4 >= 800:
                second_step = Player.y4 - 800
                Player.y4 = 700
                Player.x4 -= second_step
                Player.x4 -= 100

        elif player_sequence == 4 and Player.x4 < 1000 and Player.y4 == 700:
            Player.x4 -= step * 100
            if Player.x4 <= 0:
                second_step = 0 - Player.x4
                Player.x4 = 0
                Player.y4 = 700 - second_step

        elif player_sequence == 4 and Player.x4 == 0 and Player.y4 <= 700:
            Player.y4 -= step * 100
            if Player.y4 <= 0:
                second_step = 0 - Player.y4
                Player.y4 = 0
                Player.x4 = second_step

    def show_players():
        screen.blit(Player.p1, (Player.x1, Player.y1))
        screen.blit(Player.p2, (Player.x2, Player.y2))
        screen.blit(Player.p3, (Player.x3, Player.y3))
        screen.blit(Player.p4, (Player.x4, Player.y4))

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
                player_dict_m['p1_money'] += 2000
                print(f"player 1 passes go and get 2000")
                print(f"Player 1 is now at: {player1_pos}")
            else:
                player1_pos -= 32
                player_dict_m['p1_money'] += 2000
                print(f"player 1 passes go and get 2000")
                print(f"Player 1 is now at: {player1_pos}")

        if dice_con and dice_rolled and player_sequence == 2:
            dice_rolled = False
            print(f"dice is {dice_num}")
            player2_pos = player2_pos + dice_num
            if player2_pos < 32:
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
        if dice_con and dice_rolled and player_sequence == 3:
            dice_rolled = False
            print(f"dice is {dice_num}")
            player3_pos = player3_pos + dice_num
            if player3_pos < 32:
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

        if dice_con and dice_rolled and player_sequence == 4:
            dice_rolled = False
            print(f"dice is {dice_num}")

            player4_pos = player4_pos + dice_num
            if player4_pos < 32:
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


active_player_index = 0

total_positions = num_row * 2 + num_col * 2 - 4


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
            chance_rarity = determine_chance_rarity(second_roll)
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

    if player_sequence == 1:
        if player2_pos == 12 or player2_pos == 28:
            second_roll = random.randint(1, 6)
            chance_rarity = determine_chance_rarity(second_roll)
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

    if player_sequence == 2:
        if player3_pos == 12 or player3_pos == 28:
            second_roll = random.randint(1, 6)
            chance_rarity = determine_chance_rarity(second_roll)
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

    if player_sequence == 3:
        if player4_pos == 12 or player4_pos == 28:
            second_roll = random.randint(1, 6)
            chance_rarity = determine_chance_rarity(second_roll)
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


# settings for the property
price = 0
# price list is for player to buy property according to their price
Pricelist = [0, 500, 600, 700, 0, 2100, 800, 900, 1000, 0, 1200, 1300, 0, 1400, 1500, 1600,
             0, 1800, 1900, 2000, 0, 2150, 2200, 2400, 2500, 0, 2600, 2800, 0, 3000, 3500, 4000]

name_list = ['Passngo', 'Ramly Burger', '99 Speedmarket', 'Aeon Big', 'tax', 'TNB', 'Batu Caves', 'Pulau Langkawi', 'Cameron Highland', 'parking', 'Gunung Mulu', 'Mount Kinabalu', 'chance', 'Johor Bahru', 'George Town',
             'Melaka', 'jail', 'KL Sentral', 'Port Dickson', 'MMU Cyberjaya', 'tax', 'Indah water', 'Genting Highland', 'Putrajaya', 'KLIA', 'injail', 'TRX', 'Pavilion KL', 'chance', 'KL Tower', 'Merdeka 118', 'KLCC']

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
    eco_dis1 = str()
    eco_dis2 = str()
    eco_dis3 = str()
    eco_dis4 = str()
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
    # checking for price is 0 for validity of buying

    def check_buying_valid():
        if player_sequence == 1 and player1_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            if Pricelist[player1_pos] != 0:
                button_buy.update()

        elif player_sequence == 2 and player2_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            if Pricelist[player2_pos] != 0:
                button_buy.update()

        elif player_sequence == 3 and player3_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            if Pricelist[player3_pos] != 0:
                button_buy.update()

        elif player_sequence == 4 and player4_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            if Pricelist[player4_pos] != 0:
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
        middle = 0
        if player_sequence == 1 and Pricelist[player1_pos] != 0:
            b_property = [
                i for i in Property_with_price if Property_with_price[i] == price]
            b_property = ', '.join(b_property)
            p1_list_p.append(b_property)
            economic.eco_dis1 = (f'Player 1 paid {price} for {b_property} ')
            if len(p1_list_p) > 5:
                middle = len(p1_list_p)//2
                economic.leco_dis1 = p1_list_p[:middle]
                economic.L_eco_dis1 = p1_list_p[middle:]
                economic.leco_dis1 = (f'own {economic.leco_dis1}')
            else:
                economic.leco_dis1 = (f'own {p1_list_p}')

            print(economic.eco_dis1)
            Pricelist[player1_pos] = 0
        elif player_sequence == 2 and Pricelist[player2_pos] != 0:
            b_property = [
                i for i in Property_with_price if Property_with_price[i] == price]
            b_property = ', '.join(b_property)
            p2_list_p.append(b_property)
            economic.eco_dis2 = (f'player 2 paid {price} for {b_property} ')
            if len(p2_list_p) > 5:
                middle = len(p2_list_p)//2
                economic.leco_dis2 = p2_list_p[:middle]
                economic.L_eco_dis2 = p2_list_p[middle:]
                economic.leco_dis2 = (f'own {economic.leco_dis2}')
            else:
                economic.leco_dis2 = (f'own {p2_list_p}')
            print(economic.eco_dis2)
            Pricelist[player2_pos] = 0
        elif player_sequence == 3 and Pricelist[player3_pos] != 0:
            b_property = [
                i for i in Property_with_price if Property_with_price[i] == price]
            b_property = ', '.join(b_property)
            p3_list_p.append(b_property)
            economic.eco_dis3 = (f'player 3 paid {price} for {b_property} ')
            if len(p3_list_p) > 5:
                middle = len(p3_list_p)//2
                economic.leco_dis3 = p3_list_p[:middle]
                economic.L_eco_dis3 = p3_list_p[middle:]
                economic.leco_dis3 = (f'own {economic.leco_dis3}')
            else:
                economic.leco_dis3 = (f'own {p3_list_p}')
            print(economic.eco_dis3)
            Pricelist[player3_pos] = 0
        elif player_sequence == 4 and Pricelist[player4_pos] != 0:
            b_property = [
                i for i in Property_with_price if Property_with_price[i] == price]
            b_property = ', '.join(b_property)
            p4_list_p.append(b_property)
            economic.eco_dis4 = (f'player 4 paid {price} for {b_property} ')
            if len(p4_list_p) > 5:
                middle = len(p4_list_p)//2
                economic.leco_dis4 = p4_list_p[:middle]
                economic.L_eco_dis4 = p4_list_p[middle:]
                economic.leco_dis4 = (f'own {economic.leco_dis4}')
            else:
                economic.leco_dis4 = (f'own {p4_list_p}')
            print(economic.eco_dis4)
            Pricelist[player4_pos] = 0

        else:
            pass

    def update_eco():
        global player_sequence
        title_font = pygame.font.Font("HelveticaNeue.ttf", 18)
        rent_font = pygame.font.Font("HelveticaNeue.ttf", 20)
        dis_eco1 = economic.eco_dis1
        dis_eco2 = economic.eco_dis2
        dis_eco3 = economic.eco_dis3
        dis_eco4 = economic.eco_dis4
        ldis_eco1 = economic.leco_dis1
        ldis_eco2 = economic.leco_dis2
        ldis_eco3 = economic.leco_dis3
        ldis_eco4 = economic.leco_dis4
        L_dis_eco1 = economic.L_eco_dis1
        L_dis_eco2 = economic.L_eco_dis2
        L_dis_eco3 = economic.L_eco_dis3
        L_dis_eco4 = economic.L_eco_dis4
        rent_display = economic.rent_display
        dis_eco1 = title_font.render(f"{dis_eco1}", True, black)
        ldis_eco1 = title_font.render(f"{ldis_eco1}", True, black)
        L_dis_eco1 = title_font.render(f"{L_dis_eco1}", True, black)
        dis_eco2 = title_font.render(f"{dis_eco2}", True, black)
        ldis_eco2 = title_font.render(f"{ldis_eco2}", True, black)
        L_dis_eco2 = title_font.render(f"{L_dis_eco2}", True, black)
        dis_eco3 = title_font.render(f"{dis_eco3}", True, black)
        ldis_eco3 = title_font.render(f"{ldis_eco3}", True, black)
        L_dis_eco3 = title_font.render(f"{L_dis_eco3}", True, black)
        dis_eco4 = title_font.render(f"{dis_eco4}", True, black)
        ldis_eco4 = title_font.render(f"{ldis_eco4}", True, black)
        L_dis_eco4 = title_font.render(f"{L_dis_eco4}", True, black)
        rent_display = rent_font.render(f"{rent_display}", True, black)
        # showing player current activity
        if player_sequence == 1 and not paying:
            screen.blit(dis_eco1, (120, 630))
            screen.blit(ldis_eco1, (120, 650))
            screen.blit(L_dis_eco1, (120, 670))
        elif player_sequence == 2 and not paying:
            screen.blit(dis_eco2, (120, 630))
            screen.blit(ldis_eco2, (120, 650))
            screen.blit(L_dis_eco2, (120, 670))
        elif player_sequence == 3 and not paying:
            screen.blit(dis_eco3, (120, 630))
            screen.blit(ldis_eco3, (120, 650))
            screen.blit(L_dis_eco3, (120, 670))
        elif player_sequence == 4 and not paying:
            screen.blit(dis_eco4, (120, 630))
            screen.blit(ldis_eco4, (120, 650))
            screen.blit(L_dis_eco4, (120, 670))
        elif player_sequence != 0 and paying:
            screen.blit(rent_display, (120, 630))

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
                player_dict_m['p1_money'] -= rent_price
                player_dict_m['p2_money'] += rent_price
                print(f"Player 1 now have {player_dict_m['p1_money']}")
                print(f"Player 2 now have {player_dict_m['p2_money']}")
                paying = False

            if property_rent in p3_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 3")
                print(f"Player 1 paying {rent_price} for player 3")
                player_dict_m['p1_money'] -= rent_price
                player_dict_m['p3_money'] += rent_price
                print(f"Player 1 now have {player_dict_m['p1_money']}")
                print(f"Player 3 now have {player_dict_m['p3_money']}")
                paying = False

            if property_rent in p4_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 4")
                print(f"Player 1 paying {rent_price} for player 4")
                player_dict_m['p1_money'] -= rent_price
                player_dict_m['p4_money'] += rent_price
                print(f"Player 1 now have {player_dict_m['p1_money']}")
                print(f"Player 4 now have {player_dict_m['p4_money']}")
                paying = False

            else:
                paying == False

    def rent_button_2():
        global paying
        if player_sequence == 2 and player2_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            property_rent = name_list[player2_pos]
            # checking for a property is not own by player 2
            if property_rent in p1_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 1")
                print(f"Player 2 paying {rent_price} for player 1")
                player_dict_m['p2_money'] -= rent_price
                player_dict_m['p1_money'] += rent_price
                print(f"Player 2 now have {player_dict_m['p2_money']}")
                print(f"Player 1 now have {player_dict_m['p1_money']}")
                paying = False
            if property_rent in p3_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 3")
                print(f"Player 2 paying {rent_price} for player 3")
                player_dict_m['p2_money'] -= rent_price
                player_dict_m['p3_money'] += rent_price
                print(f"Player 2 now have {player_dict_m['p2_money']}")
                print(f"Player 2 now have {player_dict_m['p2_money']}")
                paying = False
            if property_rent in p4_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 4")
                print(f"Player 2 paying {rent_price} for player 4")
                player_dict_m['p2_money'] -= rent_price
                player_dict_m['p4_money'] += rent_price
                print(f"Player 2 now have {player_dict_m['p2_money']}")
                print(f"Player 4 now have {player_dict_m['p4_money']}")
                paying = False
            else:
                pass

    def rent_button_3():
        global paying
        if player_sequence == 3 and player3_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            property_rent = name_list[player3_pos]
            # checking for a property is not own by player 3
            if property_rent in p1_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 1")
                print(f"Player 3 paying {rent_price} for player 1")
                player_dict_m['p3_money'] -= rent_price
                player_dict_m['p1_money'] += rent_price
                print(f"Player 3 now have {player_dict_m['p3_money']}")
                print(f"Player 1 now have {player_dict_m['p1_money']}")
                paying = False
            if property_rent in p2_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 2")
                print(f"Player 3 paying {rent_price} for player 2")
                player_dict_m['p3_money'] -= rent_price
                player_dict_m['p2_money'] += rent_price
                print(f"Player 3 now have {player_dict_m['p3_money']}")
                print(f"Player 2 now have {player_dict_m['p2_money']}")
                paying = False
            if property_rent in p4_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 4")
                print(f"Player 3 paying {rent_price} for player 4")
                player_dict_m['p3_money'] -= rent_price
                player_dict_m['p4_money'] += rent_price
                print(f"Player 3 now have {player_dict_m['p3_money']}")
                print(f"Player 4 now have {player_dict_m['p4_money']}")
                paying = False
            else:
                pass

    def rent_button_4():
        global paying
        if player_sequence == 4 and player4_pos not in [0, 4, 9, 12, 16, 20, 25, 28]:
            property_rent = name_list[player4_pos]
            # checking for a property is not own by player 4
            if property_rent in p1_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 1")
                print(f"Player 4 paying {rent_price} for player 1")
                player_dict_m['p4_money'] -= rent_price
                player_dict_m['p1_money'] += rent_price
                print(f"Player 4 now have {player_dict_m['p4_money']}")
                print(f"Player 1 now have {player_dict_m['p1_money']}")
                paying = False

            if property_rent in p2_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 2")
                print(f"Player 4 paying {rent_price} for player 2")
                player_dict_m['p4_money'] -= rent_price
                player_dict_m['p2_money'] += rent_price
                print(f"Player 4 now have {player_dict_m['p4_money']}")
                print(f"Player 2 now have {player_dict_m['p2_money']}")
                paying = False

            if property_rent in p3_list_p:
                rent_price = Property_with_rent[property_rent]
                print(f"{property_rent} is own by player 3")
                print(f"Player 4 paying {rent_price} for player 3")
                player_dict_m['p4_money'] -= rent_price
                player_dict_m['p3_money'] += rent_price
                print(f"Player 4 now have {player_dict_m['p4_money']}")
                print(f"Player 3 now have {player_dict_m['p3_money']}")
                paying = False
            else:
                pass

    print(player_dict_m)


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


button_functions = [button_music.checkmusic, button_roll.checkroll, button_pay.check_pay,
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

    if not Display.show_loading_done and not Button.loading:
        Display.show_loading()

    if not Button.menu and not Button.loading and Display.show_loading_done:

        map.draw()
        Display.middle()
        Display.showing_dim_button()
        Display.showing_player_money()
        Display.showing_properties_name()
        economic.update_eco()
        economic.update_eco()
        button_music.update()
        button_roll.update()
        Player.show_players()
        economic.check_buying_valid()
        moving_sprites.draw(screen)
        moving_sprites.update()
        economic.check_buying_valid()
        if paying:
            button_pay.update()
        economic.check_buying_valid()
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_button_events(pygame.mouse.get_pos())
            display_description_block(pygame.mouse.get_pos())

        # if roll dice randomize a num
            if Button.rolling_con:
                Dice.rand_a_dice()
                if not paying:

                    dice_num = (random.randint(1, 6))
                    # dice animating
                    dice.animate(dice_num)
                    Player.player_movement(dice_num)
                    Button.rolling_con = False
                    buy_clicked = False

                if player_sequence != 5 and not changing_round and not paying:
                    Player.move(dice_num)
                    economic.checking_rent_valid()

            elif Button.is_buying_properties and not buy_clicked:
                economic.buying_property()

                buy_clicked = True
                Button.is_buying_properties == False
            else:
                pass

    # if player1_pos == 12 or player1_pos == 28:
    #     handle_chance()
    # if player2_pos == 12 or player2_pos == 28:
    #     handle_chance()
    # if player3_pos == 12 or player3_pos == 28:
    #     handle_chance()
    # if player4_pos == 12 or player4_pos == 28:
    #     handle_chance()

    pygame.display.update()
pygame.quit()
