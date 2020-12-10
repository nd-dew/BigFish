import pygame
import some random shit

class Enemy():
    def __init__(self, screen_game, ):
        # This should generate enemy randomly 
        self.image= pygame.image.load("resources\images\logo_shark.png")
        self.rect=self.image.get_rect() # x,y, hights, width
        self.speed=1    
        self.size=0