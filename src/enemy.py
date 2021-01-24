import pygame as pg
from random import randrange

class Enemy():
    """
    This class creates an enemy and updates its attributes. Uses random function to positioning of the enemies into
    the game window called from biggerFish. Takes the enemy attributes from settings and uses them to randomly
    spawn enemies from the top of the screen. Updates the enemy position, speed and the image

    Parameters
    ----------
    game : BiggerFish

    Attributes
    ----------
    rand_index : int
    size : int

    """
    def __init__(self, game, custom_index=None):
        rand_index = randrange(len(game.settings.enemies)) # for random creation of the enemis
        if custom_index != None:
            rand_index = custom_index

        self.speed = game.settings.enemies[rand_index].speed
        self.size = game.settings.enemies[rand_index].size

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect() # creating the rectangle of the whole screen
        # Paths to the sprite images from the list of enemy types of the Settings class
        self.sprites = [pg.image.load(game.settings.enemies[rand_index].img_path_R).convert_alpha(),
                        pg.image.load(game.settings.enemies[rand_index].img_path_S).convert_alpha(),
                        pg.image.load(game.settings.enemies[rand_index].img_path_L).convert_alpha()]

        self.current_sp = 0 # initialization of the sprite image
        self.img = self.sprites[self.current_sp]
        self.img = pg.transform.scale(self.img,  self.size) # adjusting initial size
        self.rect = self.img.get_rect() # x,y, heights, width
        self.screen_margin = self.size[0] // 2 # first element is width
        self.x_pos = randrange(0+self.screen_margin, game.settings.screen_width-self.screen_margin)
        self.y_pos = 0
        # self.rect=pg.Rect(0,0,*self.size)
        self.rect.midbottom = (self.x_pos, self.y_pos)

        # Dynamic Hitbox
        self.hitbox = pg.Rect(
                       self.rect.x + self.rect.w // 3.3,
                       self.rect.y + self.rect.h // 8,
                       self.rect.w - self.rect.w // 1.7,
                       self.rect.h - self.rect.h // 5
        )

        self.hitbox_offset_and_size = game.settings.enemies[rand_index].hitbox_offset_and_size


    def update(self, debugMode= False):
        """
        Updating the enemy's position, image and hitbox.

        Parameters
        ----------
        debugMode

        """
        if not debugMode:
            self.y_pos += self.speed
            self.rect.midbottom = (self.x_pos, self.y_pos)
        self.sprite_image()

        # Dynamic Hitbox, hardcoded
        self.hitbox = pg.Rect(
                       self.rect.x + self.rect.w // 3.3,
                       self.rect.y + self.rect.h // 8,
                       self.rect.w - self.rect.w // 1.7,
                       self.rect.h - self.rect.h // 5
        )

        self.hitbox = pg.Rect(
            self.rect.x + self.hitbox_offset_and_size[0],
            self.rect.y + self.hitbox_offset_and_size[1],
            self.hitbox_offset_and_size[2],
            self.hitbox_offset_and_size[3]
        )


    def blit_enemy(self, bbox=False, hitbox=False):
        """
        Drawing enemies into the screen.

        Parameters
        ----------
        bbox : boolean
        hitbox

        Returns
        -------

        """
        self.screen.blit(self.img, self.rect)  # blit() method draws the image on top
        if bbox:
            pg.draw.rect(self.screen, pg.Color('green'), self.rect, width=1)
        if hitbox:
            pg.draw.rect(self.screen, pg.Color('red'), self.hitbox, width=1)

    def sprite_image(self):
        """
        Algorithm for repeating the three sprite images (incement od 0.3)
        """
        self.current_sp += 0.3
        if self.current_sp >= len(self.sprites):
            self.current_sp = 0
        self.img = self.sprites[int(self.current_sp)]
        self.img = pg.transform.scale(self.img,  self.size) # adjusting size
