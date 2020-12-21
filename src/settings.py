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
        self.screen_size=(self.screen_width, self.screen_height)

        self.bg_color= (230, 230, 230)

        self.bg_img_path = 'resources/images/under_the_sea.png'

        self.logo_path = "resources/images/logo_shark.png"
        self.FPS = 60

