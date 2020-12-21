from src.enemyType import EnemyType

class Settings:
    """
    Class designed to hold all constants in the game. maybe more?

     Attributes
    ----------
    screen_width : int
        horizontal size of main game screen in pixels
    screen_height : bool
        vertical size of main game screen in pixels
    screen_size : (int, int)
        current state of left arrow key True if pressed
    FPS : int
        number of maximum frames per second
    bg_color: (int, int, int)
        depricated rgb background color
    logo_path: str
        path to logo image
    """

    def __init__(self):
        self.screen_width = 600
        self.screen_height = 600
        self.screen_size = (self.screen_width, self.screen_height)

        self.bg_color = (230, 230, 230)
        self.bg_img_path = 'resources/images/under_the_sea.png'

        self.logo_path = "resources/images/logo_shark.png"
        self.FPS = 60

        # PLAYER SPRITE PICTURES
        self.player_steady = "resources/images/sprite_sheets/tile037.png"
        self.player_tailRight = "resources/images/sprite_sheets/tile036.png"
        self.player_tailLeft = "resources/images/sprite_sheets/tile038.png"

        # ENEMIES
        """(speed, width, height, path_R, path_S, path_L)"""
        red_fish = EnemyType(1, width=48, height=48, path_R="resources/images/enemy2.png", path_S="resources/images/enemy1.png", path_L="resources/images/enemy3.png")
        green_fish = EnemyType(1, width=60, height=60, path_R="resources/images/enemy5.png", path_S="resources/images/enemy4.png", path_L="resources/images/enemy6.png")
        brown_fish = EnemyType(3, width=100, height=100, path_R="resources/images/enemy8.png", path_S="resources/images/enemy7.png", path_L="resources/images/enemy9.png")

        self.enemies = [red_fish, green_fish, brown_fish]