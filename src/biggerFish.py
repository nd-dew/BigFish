import random
import pygame
from src import settings
from src import player
from src.state import State
from src.controls import Controls
from src.sprite import Sprite

class BiggerFish:
    def __init__(self):
        pygame.init()
        self.settings = settings.Settings()

        pygame.display.set_caption('Bigger Fish')
        icon = pygame.image.load(self.settings.logo_path)
        pygame.display.set_icon(icon)
        self.screen = pygame.display.set_mode(self.settings.screen_size)  # screen is a tuple of width and height

        self.clock = pygame.time.Clock()  # for frames per second/ delay?
        self.enemies = []
        self.score = 0  # initializing counter

        self.player = player.Player(self)  # player instance
        self.running = True

        self.controls= Controls()
        
        self.bg_surface= pygame.image.load('resources/images/under_the_sea.png')
        self.bg_surface= pygame.transform.scale(self.bg_surface, self.settings.screen_size)

        self.bubble=Sprite('resources/images/sprite_sheets/water_bubbles/water_bubbles.xml', [387,290])

    def run_game(self):
        while self.running:  # Start of the game's main loop
            self.check_events()  # Event loop
            self.player.update(self.controls.what_fish_should_do())  # Checking the update method in PLAYER each loop.
            self.screen_update()  # Updating screen
            self.clock.tick(self.settings.FPS)
            print(self.controls) # DEBUG

    def spawn(self):
        # create instance of enemy and append local list
        pass

    def check_events(self):
        for event in pygame.event.get():
            
            # QUIT GAME
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                self.running = False

            # KEYBOARD INPUT
            elif event.type == pygame.KEYDOWN:  # Check for events when a keypress is done
                if event.key == pygame.K_RIGHT:
                    self.player.direction = "right"
                    self.controls.right_down()
                elif event.key == pygame.K_LEFT:
                    self.player.direction = "left"
                    self.controls.left_down()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.direction = "stop"
                    self.controls.right_up()
                elif event.key == pygame.K_LEFT:
                    self.player.direction = "stop"
                    self.controls.left_up()

    def screen_update(self):
        self.screen.fill(self.settings.bg_color)  # Redrawing the background each pass
        self.screen.blit(self.bg_surface, [0,0])
        self.player.blit_player()  # drawing our fish on top of our background
        # blit enemies in the screen (iterate over self.enemies )
        self.bubble.blit(self.screen)
        pygame.display.flip()  # TODO change to update
