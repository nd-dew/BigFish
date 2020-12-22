import pygame
from random import randrange

class Enemy():
    def __init__(self, game):
        rand_index = randrange(len(game.settings.enemies))
        # This should generate enemy randomly 
        self.speed = game.settings.enemies[rand_index].speed
        # self.size = [24, 48] # width, height
        self.size = game.settings.enemies[rand_index].size

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect() # creating the rectangle of the whole screen

        # random_enemy = randrange(0,3)
        self.sprites = []
        self.sprites.append(pygame.image.load(game.settings.enemies[rand_index].img_path_R).convert())
        self.sprites.append(pygame.image.load(game.settings.enemies[rand_index].img_path_S).convert())
        self.sprites.append(pygame.image.load(game.settings.enemies[rand_index].img_path_L).convert())

        self.current_sp = 0
        self.img = self.sprites[self.current_sp]
        self.img = pygame.transform.scale(self.img,  self.size) # adjusting initial size
        self.rect = self.img.get_rect() # x,y, heights, width
        self.screen_margin = self.size[0] // 2 # first element is width
        self.x_pos = randrange(0+self.screen_margin, game.settings.screen_width-self.screen_margin)
        self.y_pos = 0
        self.rect.midbottom = (self.x_pos, self.y_pos)

    def update(self):
        self.y_pos += self.speed
        self.sprite_image()
        self.rect.midbottom = (self.x_pos, self.y_pos)

    def blit_enemy(self, bbox=False):
        if bbox :
            pygame.draw.rect(self.img, pygame.Color('red'), [0,0,self.rect.width,self.rect.height], width=1)
        self.screen.blit(self.img, self.rect)  # blit() method draws the image on top

    def sprite_image(self):
        self.current_sp += 0.3
        if self.current_sp >= len(self.sprites):
            self.current_sp = 0
        self.img = self.sprites[int(self.current_sp)]
        self.img = pygame.transform.scale(self.img,  self.size) # adjusting size
