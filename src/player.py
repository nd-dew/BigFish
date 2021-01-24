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
        How fast player moves per tick
    screen : pg.surface
        local copy of main screen used in main game class
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
    TODO update above documentation
    """

    def __init__(self, game):
        self.speed = 5
        self.biggerFish= game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect() # creating the rectangle of the whole screen used to position the player at the right location

        # Getting player sprites
        self.sprites = {'steady': pg.image.load(game.settings.player_steady).convert_alpha(),
                        'tailRight': pg.image.load(game.settings.player_tailRight).convert_alpha(),
                        'tailLeft': pg.image.load(game.settings.player_tailLeft).convert_alpha()}

        # Initial image rescaling
        self.img = self.sprites['steady']
        self.rect = self.img.get_rect()

        # Setting initial position
        self.rect.midbottom = self.screen_rect.midbottom # midbottom point of the screen is set to be equal with  midbnottom point of the player

        self.right = False # initial movement to the right
        self.left = False # initial movement to the left

        # Dynamic Hitbox, hardcoded
        self.hitbox = pg.Rect(self.rect.x + 12, self.rect.y+5, self.rect.w - 27, self.rect.h-13)

    def update(self, score=0):
        """
        Method called from the biggerFish class to update the player's x-coordinate and based on the movement also
        sprite pictures.
        """
        self._grow_if_ready(score)

        if self.right and not self.left and self.rect.right < self.screen_rect.right: # ...and player movement range restriction
            self.rect.x += self.speed
            self.img = self.sprites["tailLeft"]
            self.img = pg.transform.scale(self.img, [self.rect.w, self.rect.h])
        elif self.left and not self.right and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.speed
            self.img = self.sprites["tailRight"]
            self.img = pg.transform.scale(self.img, [self.rect.w, self.rect.h])

        else:
            self.img = self.sprites["steady"]
            self.img = pg.transform.scale(self.img, [self.rect.w, self.rect.h])

        # # Dynamic Hitbox, hardcoded again
        # self.hitbox = pg.Rect(self.rect.x + 13, self.rect.y+2, self.rect.w - 27, self.rect.h-13)


    def blit_player(self, bbox=False, hitbox=False):
        """
        Render player img on screen surface
        """
        self.screen.blit(self.img, self.rect)  # blit() method draws the image on top
        if bbox:
            pg.draw.rect(self.screen, pg.Color('green'), self.rect, width=1) # box of the image
        if hitbox:
            pg.draw.rect(self.screen, pg.Color('red'), self.hitbox, width=1)

    def change_size(self, level):
        """
        Modify current sprite set into chosen one.

        Parameters
        ----------
        level : int
            specify which dict of sprites should be used (among sizes)
        """
        self.size_level = level

    def _grow_if_ready(self, score):
        """
        Based on the parameters in Settings, the method check whether the number of points has reached the threshold
        Parameters.
        ----------
        score : int

        """

        # iterate over thresholds and compare them with current score
        reached_threshold = 0
        for threshold in self.biggerFish.settings.player_sizes.keys():
            if score >= threshold:
                reached_threshold=threshold
        self.rect.w = self.biggerFish.settings.player_sizes[reached_threshold]['width']
        self.rect.h = self.biggerFish.settings.player_sizes[reached_threshold]['height']
        self.rect.bottom = self.screen_rect.bottom + self.biggerFish.settings.player_sizes[reached_threshold]['y_offset']
        hitbox_offset_and_size = self.biggerFish.settings.player_sizes[reached_threshold]['hitbox_offset_and_size']
        self.hitbox = pg.Rect(
                self.rect.x + hitbox_offset_and_size[0],
                self.rect.y + hitbox_offset_and_size[1],
                hitbox_offset_and_size[2],
                hitbox_offset_and_size[3]
        )

