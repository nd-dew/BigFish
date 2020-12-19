import pygame

class Player():
    def __init__(self, game):
        self.speed = 1
        self.size = [int(48*2), int(48*2)] # [width, height]

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect() # creating the rectangle of the whole screen

        # Getting player sprites
        self.sprites={}
        self.sprites['steady'] = pygame.image.load("resources/images/sprite_sheets/tile037.png").convert()
        self.sprites['tailRight'] = pygame.image.load("resources/images/sprite_sheets/tile036.png").convert()
        self.sprites['tailLeft'] = pygame.image.load("resources/images/sprite_sheets/tile038.png").convert()

        # Initial image rescaling
        self.img = self.sprites['steady']
        self.img = pygame.transform.scale(self.img,  self.size)
        self.rect = self.img.get_rect()

        # Setting initial position
        self.rect.midbottom = self.screen_rect.midbottom # midbottom point of the screen is set to be equal with  midbnottom point of the player



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