import pygame as pg
from src.enemyType import EnemyType
import random

class Settings:
    """
    Class designed to hold all constants in the game. This includes Basic game window parameters, graphical image
    animations (for background, player sprite images, enemies sprite images). Setting of frames per seconds. This
    class also includes a list of different enemy types with all of their attributes (speed, size, image path) as
    well as a dictionary of different evolution steps of the player.

     Attributes
    ----------
    screen_width : int
        horizontal size of main game screen in pixels
    screen_height : int
        vertical size of main game screen in pixels
    screen_size : (int, int)
        current state of left arrow key True if pressed
    FPS : int
        number of maximum frames per second
    bg_color: (int, int, int)
        depricated rgb background color
    bg_animation : list
        list of background animation images
    score_text : pygame image
        image used underneath the score text field
    game_over_img : pygame image
        image used for gameover Scene
    logo_path: str
        path to logo image
    player_steady : String
        path to image with a steady tail of the player
    player_tailRight : String
        path to image with a left curved tail of the player
    player_tailLeft : String
        path to image with a right curved tail of the player
    enemies : list
        list of enemy types
    player_sizes : dictionary
        dictionary of player sizes

    """

    def __init__(self):
        self.screen_width = 500
        self.screen_height = 500
        self.screen_size = (self.screen_width, self.screen_height)
        self.bg_color = pg.Color('gray')

        # BACKGROUND SPRITE PICTURES
        self.bg_animation = []
        for i in range(0, 49):
            string1 = 'resources/images/background/bg' + str(i) + '.png'
            self.bg_animation.append(pg.image.load(string1))
        self.score_text = pg.image.load('resources/images/background/score.png')

        # MAIN MENU SPRITE PICTURES
        self.main_menu_animation = []
        for j in range(0, 28):
            string2 = 'resources/images/main_menu/main_menu_' + str(j) + '.png'
            self.main_menu_animation.append(pg.image.load(string2))
        self.main_menu_text = pg.image.load("resources/images/main_menu/all_menu.png")

        # GAME OVER IMAGE
        self.game_over_img = pg.image.load("resources/images/main_menu/game_over.png")

        # LOGO PATH
        self.logo_path = "resources/images/logo.png"

        # FRAMES PER SECOND
        self.FPS = 60

        # PLAYER SPRITE PICTURES
        self.player_steady = "resources/images/player/player0.png"
        self.player_tailRight = "resources/images/player/player1.png"
        self.player_tailLeft = "resources/images/player/player2.png"

        # ENEMIES
        """(speed, width, height, [x_hitbox_offset, y_hitbox_offset, x_hitbox_size, y_hitbox_size], path_R, path_S, path_L)"""
        red_fish = EnemyType(       speed=random.uniform(4.75,5.25), width=15,  height= 15, hitbox_offset_and_size=[1,0,14,15], path_R="resources/images/enemies/red1.png", path_S="resources/images/enemies/red2.png", path_L="resources/images/enemies/red3.png")
        green_fish = EnemyType(     speed=random.uniform(1.75,2.25), width=40,  height= 60, hitbox_offset_and_size=[5,0,30,60], path_R="resources/images/enemies/green1.png", path_S="resources/images/enemies/green2.png", path_L="resources/images/enemies/green3.png")
        brown_fish = EnemyType(     speed=random.uniform(2.75,3.25), width=40,  height= 50, hitbox_offset_and_size=[4,0,30,50], path_R="resources/images/enemies/brown1.png", path_S="resources/images/enemies/brown2.png", path_L="resources/images/enemies/brown3.png")
        white_fish = EnemyType(     speed=random.uniform(3.75,4.25), width=20,  height= 20, hitbox_offset_and_size=[2,0,20,20], path_R="resources/images/enemies/white1.png", path_S="resources/images/enemies/white2.png", path_L="resources/images/enemies/white3.png")
        blue_fish = EnemyType(      speed=random.uniform(3.75,4.25), width=30,  height= 30, hitbox_offset_and_size=[4,0,24,30], path_R="resources/images/enemies/blue1.png", path_S="resources/images/enemies/blue2.png", path_L="resources/images/enemies/blue3.png")
        ray_fish = EnemyType(       speed=random.uniform(2.75,3.25), width=80, height=100, hitbox_offset_and_size=[15,0,50,100], path_R="resources/images/enemies/ray1.png", path_S="resources/images/enemies/ray2.png", path_L="resources/images/enemies/ray3.png")
        x_blue_fish = EnemyType(    speed=random.uniform(2.75,3.25), width=60,  height= 60, hitbox_offset_and_size=[13,0,35,60], path_R="resources/images/enemies/xblue1.png", path_S="resources/images/enemies/xblue2.png", path_L="resources/images/enemies/xblue3.png")
        x_pink_fish = EnemyType(    speed=random.uniform(2.75,3.25), width=60,  height= 60, hitbox_offset_and_size=[13,0,35,60], path_R="resources/images/enemies/xpink1.png", path_S="resources/images/enemies/xpink2.png", path_L="resources/images/enemies/xpink3.png")
        blow_fish = EnemyType(      speed=random.uniform(0.75,1.25), width=50,  height= 50, hitbox_offset_and_size=[8,0,30,50], path_R="resources/images/enemies/blow1.png", path_S="resources/images/enemies/blow2.png", path_L="resources/images/enemies/blow3.png")
        sblow_fish = EnemyType(     speed=random.uniform(2.75,3.25), width=60,  height= 60, hitbox_offset_and_size=[15,0,28,60], path_R="resources/images/enemies/sblow1.png", path_S="resources/images/enemies/sblow2.png", path_L="resources/images/enemies/sblow3.png")
        gray_fish = EnemyType(      speed=random.uniform(2.75,3.25), width=80,  height= 80, hitbox_offset_and_size=[20,0,40,78], path_R="resources/images/enemies/gray1.png", path_S="resources/images/enemies/gray2.png", path_L="resources/images/enemies/gray3.png")
        gray_shark = EnemyType(     speed=random.uniform(3.75,4.25), width=110, height=150, hitbox_offset_and_size=[30,0,50,149], path_R="resources/images/enemies/sharkgray1.png", path_S="resources/images/enemies/sharkgray2.png", path_L="resources/images/enemies/sharkgray3.png")
        black_shark = EnemyType(    speed=random.uniform(6.75,7.25), width=100, height=200, hitbox_offset_and_size=[20,0,60,200], path_R="resources/images/enemies/sharkblack1.png", path_S="resources/images/enemies/sharkblack2.png", path_L="resources/images/enemies/sharkblack3.png")
        greenorange_shark=EnemyType(speed=random.uniform(3.75,4.25), width=90, height=140, hitbox_offset_and_size=[25,0,40,140], path_R="resources/images/enemies/sharkgreenor1.png", path_S="resources/images/enemies/sharkgreenor2.png", path_L="resources/images/enemies/sharkgreenor3.png")
        pink_dolphin = EnemyType(   speed=random.uniform(4.75,5.25), width=80, height=120, hitbox_offset_and_size=[20,0,40,120], path_R="resources/images/enemies/dolphinpink1.png", path_S="resources/images/enemies/dolphinpink2.png", path_L="resources/images/enemies/dolphinpink3.png")
        blue_dolphin = EnemyType(   speed=random.uniform(3.75,4.25), width=110, height=150, hitbox_offset_and_size=[30,0,50,149], path_R="resources/images/enemies/dolphinblue1.png", path_S="resources/images/enemies/dolphinblue2.png", path_L="resources/images/enemies/dolphinblue3.png")

        self.enemies = [red_fish, green_fish, brown_fish, white_fish, blue_fish, ray_fish, x_blue_fish, x_pink_fish, blow_fish, sblow_fish, gray_fish, gray_shark, black_shark, greenorange_shark, pink_dolphin, blue_dolphin]

        # Player Evolution
        """{
        threshold: {width, height, [x_hitbox_offset ,y_hitbox_offset , hitbox_width, hitbox_height, y_offset]}
        threshold: {width, height, [x_hitbox_offset ,y_hitbox_offset , hitbox_width, hitbox_height, y_offset]}
        threshold: {width, height, [x_hitbox_offset ,y_hitbox_offset , hitbox_width, hitbox_height, y_offset]}...
        }"""
        self.player_sizes = {
            0:  dict(width=24, height=24, hitbox_offset_and_size=[0,0,24,24], y_offset=0),
            2:  dict(width=35, height=35, hitbox_offset_and_size=[4,0,28,35], y_offset=5),
            6:  dict(width=55, height=55, hitbox_offset_and_size=[10,0,35,55], y_offset=10),
            13:  dict(width=90, height=90, hitbox_offset_and_size=[17,0,55,90], y_offset=25),
        }