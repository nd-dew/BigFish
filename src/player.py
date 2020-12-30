import pygame as pg

class Player():
    """
    Player object to hold all values describing player fish. Contains also methods to modify player attr.

    Parameters
    ----------
    game : BiggerFish

    Attributes
    ----------
    speed : int
        How fast player moves per tick, (TODO would be nice to base it on time not framerate)
    size : [int, int]
        Actual size of displayed player image in pixels. [width, height]
    sizes : [[int,int], [int,int], [int,int], ...]
        List of all possible sizes player can take.
    screen : pg.surface
        local copy of main screen used in main game class (DO we really need it)
    screen_rect: pg.Rect
        rect structure derived from main screen, used in boundary case calculations
    all_sizes_sprites: {int: {str: pg.Surface, str: pg.Surface, str: pg.Surface}... }
       Dict containing all of possible images of player. Calculated in the beginning of the game.
       Data Structure Explained:
           {level_1 : dict_with_sprites, level_2 : dict_with_sprites, level_3 : dict_with_sprites...}
            it is a dictionary of dictionaries. Keys in outer dictionary are integers (so far). While in the inner dicts
            called in here 'dict_with_sprites' we find rescaled sprites.
            Structure of inner dict called in here dict_with_sprites looks like this:
            {'steady': pg.Surface, 'tailRight': pg.Surface, 'tailLeft': pg.Surface}
    sprites : {'steady': pg.Surface, 'tailRight': pg.Surface, 'tailLeft': pg.Surface}
        current set of sprites used to display animations.
    img : pg.Surface
        current image to blit on screen
    rect : pg.Rect
        rect corresponding to self.img, used to describe position in bliting
    direction : str
        deprecated, Used in past to represent current state of player
    currentState : State
        instance of imported enum struct, describes current state in which player is
    """


    def __init__(self, game):
        self.speed = game.settings.player_speed
        self.hit_widths = game.settings.player_hit_widths
        self.hit_ratio = game.settings.player_hit_ratio
        self.widths = [int(wid / self.hit_ratio) for wid in self.hit_widths] # list of widths
        self.size_level = 0 # initial size level = first element of the sizes list

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect() # creating the rectangle of the whole screen

        # Getting player sprites
        self.sprites = {'steady': pg.image.load(game.settings.player_steady).convert_alpha(), #convert_alpha preserves transparency in PNG images
                        'tailRight': pg.image.load(game.settings.player_tailRight).convert_alpha(),
                        'tailLeft': pg.image.load(game.settings.player_tailLeft).convert_alpha()}

        # Initial image rescaling
        self.img = self.sprites['steady']
        self.w_ratio = self.img.get_width() / self.img.get_height() # Width to Height ratio of the original image
        self.width = self.widths[self.size_level]
        self.height = int(self.width / self.w_ratio)
        self.size = [self.width, self.height]
        self.img = pg.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()
        # Setting initial position
        self.rect.midbottom = self.screen_rect.midbottom # midbottom point of the screen is set to be equal with  midbnottom point of the player

        self.right = False # initial movement to the right
        self.left = False # initial movement to the left

        # Dynamic Hitbox, hardcoded
        self.hitbox = self.rect.copy()
        self.hitbox.width = int(self.rect.width * self.hit_ratio)
        self.hitbox.midbottom = self.rect.midbottom

    def update(self):
        """ to be added
        """
        self.width = self.widths[self.size_level]
        self.height = int(self.width/self.w_ratio)
        self.size = [self.width, self.height]

        if self.right and not self.left and self.rect.right < self.screen_rect.right: # ...and player movement range restriction
            self.rect.x += self.speed
            self.img = self.sprites["tailLeft"]
        elif self.left and not self.right and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.speed
            self.img = self.sprites["tailRight"]
        else:
            self.img = self.sprites["steady"]

        self.img = pg.transform.scale(self.img, self.size)
        self.rect.size = self.size
        self.rect.bottom = self.screen_rect.bottom # when resizing, resetting the y coordinate of the bottom

        # Dynamic Hitbox, hardcoded again
        self.hitbox.width = int(self.rect.width * self.hit_ratio)
        self.hitbox.height = self.rect.height
        self.hitbox.midbottom = self.rect.midbottom


    def blit_player(self, bbox=False, hitbox=False):
        """
        Render player img on screen surface
        """
        if bbox :
            pg.draw.rect(self.screen, pg.Color('green'), self.rect, width=1) # box of the image
        if hitbox:
            pg.draw.rect(self.screen, pg.Color('red'), self.hitbox, width=1)
        self.screen.blit(self.img, self.rect)  # blit() method draws the image on top

    def increase_size(self):
        self.size_level += 1
