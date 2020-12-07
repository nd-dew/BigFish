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


    def run_game(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()
        player= playerFish.Player()

        while self.running: # main game loop
            # DRAW PLAYER
            # pygame.draw.rect(self.screen, (255, 255, 255), (100, 150, 20, 20))  # rect: (x1, y1, width, height)
            player.draw(self.screen)
            # EVENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()