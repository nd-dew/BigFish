import pygame
from random import randrange

class Enemy():
    def __init__(self, game):
        # This should generate enemy randomly 
        self.speed = 15
        self.size = [48,48]

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect() # creating the rectangle of the whole screen

        self.sprites = []
        random_enemy = randrange(0,3)

        if random_enemy == 0:
            self.sprites.append(pygame.image.load("resources\images\enemy1.png"))
            self.sprites.append(pygame.image.load("resources\images\enemy2.png"))
            self.sprites.append(pygame.image.load("resources\images\enemy3.png"))
        elif random_enemy == 1:
            self.sprites.append(pygame.image.load("resources\images\enemy4.png"))
            self.sprites.append(pygame.image.load("resources\images\enemy5.png"))
            self.sprites.append(pygame.image.load("resources\images\enemy6.png"))
        else:
            self.sprites.append(pygame.image.load("resources\images\enemy7.png"))
            self.sprites.append(pygame.image.load("resources\images\enemy8.png"))
            self.sprites.append(pygame.image.load("resources\images\enemy9.png"))

        self.current_sp = 0

        self.img = self.sprites[self.current_sp]

        #self.img = pygame.image.load("resources\images\enemy1.png")
        self.rect = self.img.get_rect() # x,y, heights, width

        self.random_x_pos = randrange(50,550)
        self.y_pos = 0
        self.rect.midbottom = (self.random_x_pos,self.y_pos)

    def blit_enemy(self):
        self.y_pos += 1

        self.current_sp += 0.3
        if self.current_sp >= len(self.sprites):
            self.current_sp = 0
        self.img = self.sprites[int(self.current_sp)]

        self.rect.midbottom = (self.random_x_pos, self.y_pos)
        self.screen.blit(self.img, self.rect)  # blit() method draws the image on top

    # def update(self):
    #     self.current_sp += 1
    #     if self.current_sp >= len(self.sprites):
    #         self.current_sp = 0
    #     self.img = self.sprites[self.current_sp]