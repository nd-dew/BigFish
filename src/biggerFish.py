import sys
import pygame
from src import settings
from src import player as playerFish

class BiggerFish:
    """
    """
    def __init__(self):
        pygame.init()
        self.settings= settings.Settings()

        pygame.display.set_caption('Bigger Fish')
        logo = pygame.image.load(self.settings.logo_path)
        pygame.display.set_icon(logo)

        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.running= True

        self.clock = pygame.time.Clock()

        self.player= playerFish.Player()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                self.running= False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.move("right")# Also animate in here or in inside of move
                elif event.key == pygame.K_RIGHT:
                    self.player.move("left")
            elif event.type == pygame.KEYUP:    
                elif event.key == pygame.K_RIGHT:
                    self.player.move("stop")
                elif event.key == pygame.K_RIGHT:
                    self.player.move("stop")

        

    def screen_update(self):
        self.screen.fill(self.settings.bg_color)
        # blit fish on the screen
        pygame.display.flip() # TODO learn about flip/blit

    def run_game(self): 
        while self.running:
            pass 
            # self.check events()
            # self.player.upate (calulate pos)
            # self.screen_update (render player enemys etc on the screen)
