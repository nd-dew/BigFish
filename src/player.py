import pygame

class Player():
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.img = pygame.image.load("resources/images/sprite_sheets/tile037.png") # base image
        self.rect = self.img.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.speed = 1
        self.size = 0

        self.direction = "stop"

    def update(self):
        if self.direction == "right":
            self.rect.x += self.speed
            self.img = pygame.image.load("resources/images/sprite_sheets/tile038.png")  # tail left
        elif self.direction == "left":
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