import pygame as pg
from random import randrange

class Enemy():
    def __init__(self, game):
        rand_index = randrange(len(game.settings.enemies))
        # This should generate enemy randomly 
        self.speed = game.settings.enemies[rand_index].speed
        self.width = game.settings.enemies[rand_index].width

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect() # creating the rectangle of the whole screen

        self.sprites = [pg.image.load(game.settings.enemies[rand_index].img_path_R).convert_alpha(),
                        pg.image.load(game.settings.enemies[rand_index].img_path_S).convert_alpha(),
                        pg.image.load(game.settings.enemies[rand_index].img_path_L).convert_alpha()]

        self.current_sp = 0
        self.img = self.sprites[self.current_sp]
        self.w_ratio = self.img.get_width() / self.img.get_height()
        self.height = int(self.width / self.w_ratio)
        self.size = [self.width, self.height]
        self.img = pg.transform.scale(self.img,  self.size) # adjusting initial size
        self.rect = self.img.get_rect() # x,y, heights, width
        self.screen_margin = self.size[0] // 2 # first element is width
        self.x_pos = randrange(0+self.screen_margin, game.settings.screen_width-self.screen_margin)
        self.y_pos = 0
        self.rect.midbottom = (self.x_pos, self.y_pos)

        # Dynamic Hitbox, hardcoded
        self.hitbox = self.rect.copy() # creating hitbox at the same position as the old rect
        self.hitbox.width = game.settings.enemies[rand_index].hit_width

    def update(self):
        self.y_pos += self.speed
        self.sprite_image()
        self.rect.midbottom = (self.x_pos, self.y_pos)
        self.hitbox.midbottom = self.rect.midbottom

    def blit_enemy(self, bbox=False, hitbox=False):
        if bbox:
            pg.draw.rect(self.screen, pg.Color('green'), self.rect, width=1)
        if hitbox:
            pg.draw.rect(self.screen, pg.Color('red'), self.hitbox, width=1)
        self.screen.blit(self.img, self.rect)  # blit() method draws the image on top

    def sprite_image(self):
        self.current_sp += 0.3
        if self.current_sp >= len(self.sprites):
            self.current_sp = 0
        self.img = self.sprites[int(self.current_sp)]
        self.height = int(self.width / self.w_ratio)
        self.size = [self.width, self.height]
        self.img = pg.transform.scale(self.img, self.size) # adjusting size
