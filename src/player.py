from enum import Enum
import pygame

class Player():

    def __init__(self, game):
        class State(Enum):
            stop = 1
            left = 2
            right = 3

        self.speed = 5
        self.size = [48, 48] # [width, height]
        self.sizes=[[48, 48],[60, 60],[100, 100],[120, 120],[140, 140]]

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect() # creating the rectangle of the whole screen
        self.all_sizes_sprites= self._calculate_surfaces_from_sizes(self.sizes)

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
        self.currentState= State.stop

        self.change_size(3)

    def update(self):
        if self.direction == "right" and self.rect.right < self.screen_rect.right: # ...and player movement range restriction
            self.rect.x += self.speed
            self.img = self.sprites["tailLeft"]
        elif self.direction == "left" and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.speed
            self.img = self.sprites["tailRight"]
        if self.direction == "stop": # to rethink
            self.rect.x += 0
            self.img = self.sprites["steady"]

    def blit_player(self):
        self.screen.blit(self.img, self.rect)  # blit() method draws the image on top

    def change_size(self, level):
        """
        :param level: int, specify which dict of sprites should be used in
        """
        self.sprites= self.all_sizes_sprites[level]
        position_tmp_midbottom= self.rect.midbottom
        self.rect= self.sprites["steady"].get_rect()
        self.rect.midbottom= position_tmp_midbottom

    def _calculate_surfaces_from_sizes(self, sizes):
        """
        Calculates all surfaces by rescaling to given sizes. Should be executed in the initialization
        """
        all_sizes_sprites={}
        # TODO those paths should be in one place
        steady= pygame.image.load("resources/images/sprite_sheets/tile037.png").convert()
        tailRight= pygame.image.load("resources/images/sprite_sheets/tile036.png").convert()
        tailLeft= pygame.image.load("resources/images/sprite_sheets/tile038.png").convert()
        for i, size in enumerate(sizes):
            all_sizes_sprites[i]={
                'steady':       pygame.transform.scale(steady,  size),
                'tailRight':    pygame.transform.scale(tailRight,  size),
                'tailLeft':     pygame.transform.scale(tailLeft,  size)
            }
        return all_sizes_sprites
