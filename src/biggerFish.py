import random
import pygame
from src import settings
from src import player


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

        self.controls= self.Controls()

    def run_game(self):
        while self.running:  # Start of the game's main loop
            self.check_events()  # Event loop
            self.player.update()  # Checking the update method in PLAYER each loop.
            self.screen_update()  # Updating screen
            self.clock.tick(self.settings.FPS)
            print(self.controls)

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
        self.player.blit_player()  # drawing our fish on top of our background
        # blit enemies in the screen (iterate over self.enemies )
        pygame.display.flip()  # TODO change to update

    class Controls():
        def __init__(self):
            self.keyboard={'right':False,
                           'left': False,}

        def __str__(self):
            return str(self.keyboard)

        def right_down(self):
            self.keyboard["right"]=True

        def left_down(self):
            self.keyboard["left"]=True

        def right_up(self):
            self.keyboard["right"]=False

        def left_up(self):
            self.keyboard["left"]=False


