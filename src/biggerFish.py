import sys
import pygame
from src import settings
from src import player as playerFish

class BiggerFish:
    def __init__(self):
        pygame.init()
        self.settings= settings.Settings()

        pygame.display.set_caption('Bigger Fish')
        logo = pygame.image.load(self.settings.logo_path)
        pygame.display.set_icon(logo)

        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.running= True

        self.clock = pygame.time.Clock()

    def handle_key_event(self, event_key):
        if event_key == pygame.K_ESCAPE:
            self.running = False

    def run_game(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()
        self.player= playerFish.Player()

        while self.running: # main game loop
            # DRAW BACKGROUND
            self.screen.fill(self.settings.bg_color)

            # Move Player
            self.player.check_keys_and_move()
            # DRAW PLAYER
            self.player.draw(self.screen)

            # EVENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.handle_key_event(event.key)

            pygame.display.update()
            self.clock.tick(120)
