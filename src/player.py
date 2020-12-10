import pygame

class Player():
    def __init__(self, screen_game):
        self.image= pygame.image.load("resources\images\logo_shark.png")
        self.rect=self.image.get_rect() # x,y, hights, width
        self.speed=1    
        self.size=0


    def move(self, direction):
        #animations
        pass

    def draw():
        pass
    #   blits player image on the screen 

    def change_size(self):
        pass
        # changes the size of the picture