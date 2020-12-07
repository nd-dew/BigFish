import sys
import pygame
from src import settings

class BiggerFish:
    def __init__(self):
        pygame.init()
        self.settings= settings.Settings()
        self.screen= pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_caption('Bigger Fish')

    def run_game(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()
        while True: # main game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()