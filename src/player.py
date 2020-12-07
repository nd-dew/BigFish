from operator import add

import pygame

class Player():
    def __init__(self):
        self.color=(255,255,255) # R G B
        self.position=[300, 500] # x,y
        self.size=[30, 30] # width, height

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.position + self.size )  # rect: (x1, y1, width, height)

    def move_player(self, xy):
        self.position = [self.position[0] + xy [0] , self.position[1] + xy [1] )
