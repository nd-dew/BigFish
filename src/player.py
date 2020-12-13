import pygame

class Player():
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect() # creating the rectangle of the whole screen

        self.img = pygame.image.load("resources/images/sprite_sheets/tile037.png") # base image
        self.rect = self.img.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom # midbottom point of the screen is set to be equal with  midbnottom point of the player

        self.speed = 1
        self.size = 0

        self.direction = "stop" # initial movement direction set to "stop"

    def update(self):
        if self.direction == "right" and self.rect.right < self.screen_rect.right: # ...and player movement range restriction
            self.rect.x += self.speed
            self.img = pygame.image.load("resources/images/sprite_sheets/tile038.png")  # tail left
        elif self.direction == "left" and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.speed
            self.img = pygame.image.load("resources/images/sprite_sheets/tile036.png")  # tail right
        if self.direction == "stop": # to rethink
            self.rect.x += 0
            self.img = pygame.image.load("resources/images/sprite_sheets/tile037.png")  # base image

    def blit_player(self):
        self.screen.blit(self.img, self.rect)  # blit() method draws the image on top

    def change_size(self):
        pass
        # changes the size of the picture