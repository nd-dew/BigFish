import sys
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

    def run_game(self):
        while self.running:  # Start of the game's main loop
            self.check_events()  # Event loop
            self.player.update()  # Checking the update method in PLAYER each loop.
            self.screen_update()  # Updating screen

    def spawn(self):
        # create instance of enemy and append local list
        pass

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                self.running = False
            elif event.type == pygame.KEYDOWN:  # Check for events when a keypress is done
                if event.key == pygame.K_RIGHT:
                    self.player.direction = "right"  # Also animate in here or in inside of move
                elif event.key == pygame.K_LEFT:
                    self.player.direction = "left"
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.direction = "stop"
                elif event.key == pygame.K_LEFT:
                    self.player.direction = "stop"

    def screen_update(self):
        self.screen.fill(self.settings.bg_color)  # Redrawing the background each pass
        self.player.blit_player()  # drawing our fish on top of our background
        # blit enemies in the screen (iterate over self.enemies )
        pygame.display.flip()  # TODO learn about flip/blit
