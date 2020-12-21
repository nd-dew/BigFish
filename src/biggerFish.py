import random
import pygame
from src import settings
from src import player
from src import enemy
from src.state import State
from src.controls import Controls


class BiggerFish:
    def __init__(self):
        pygame.init()
        self.settings = settings.Settings()

        pygame.display.set_caption('Bigger Fish')
        icon = pygame.image.load(self.settings.logo_path)
        pygame.display.set_icon(icon)
        self.screen = pygame.display.set_mode(self.settings.screen_size)  # screen is a tuple of width and height

        self.clock = pygame.time.Clock()  # for frames per second/ delay?
        #self.start_time = 0

        self.counter = self.Counter(self.screen)  # initializing counter

        self.enemies = [] # array of enemies
        self.spawn_rate = 2000 # initial spawn rate
        self.SPAWN_EVENT = pygame.USEREVENT
        pygame.time.set_timer(self.SPAWN_EVENT, self.spawn_rate)

        self.player = player.Player(self)  # player instance
        self.running = True

        self.controls= Controls()
        
        self.bg_surface= pygame.image.load('resources/images/under_the_sea.png')
        self.bg_surface= pygame.transform.scale(self.bg_surface, self.settings.screen_size)

    def run_game(self):
        while self.running:  # Start of the game's main loop
            self.check_events()  # Event loop
            self.player.update(self.controls.what_fish_should_do())  # Checking the update method in PLAYER each loop.
            self.counter.update(random.randint(1,1000))
            self.screen_update()  # Updating screen
            self.clock.tick(self.settings.FPS)
            #self.start_time = pygame.time.get_ticks()
            # self.spawn()
            #print(self.controls) # DEBUG

    # def spawn(self):
    #     if self.start_time > self.spawn_rate:
    #         self.enemies.append(enemy.Enemy(self))

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

            if event.type == self.SPAWN_EVENT:
                self.enemies.append(enemy.Enemy(self))

    def screen_update(self):
        self.screen.fill(self.settings.bg_color)  # Redrawing the background each pass
        self.screen.blit(self.bg_surface, [0,0])
        self.player.blit_player()  # drawing our fish on top of our background

        for enem in self.enemies:
            enem.blit_enemy()
        
        self.counter.blit(self.screen)

        # self.enemy.blit_enemy()
        # blit enemies in the screen (iterate over self.enemies )
        pygame.display.flip()  # TODO change to update

    class Counter():
        def __init__(self, parentScreen):
            self.screen=parentScreen
            self.points=0
            self.font = pygame.font.SysFont('Comic Sans MS', 30)
            self.font_color= pygame.Color('black')
            self.img= self.font.render(str(self.points), False,  self.font_color, None)
            self.rect = self.img.get_rect()

            self._move_to_bottomright_of(self.screen)

        def update(self, points):
            self.points = points
            self.img= self.font.render(str(self.points), False,  self.font_color, None)
            self.rect = self.img.get_rect()
            self._move_to_bottomright_of(self.screen)

        def _move_to_bottomright_of(self, screen):
            self.rect.bottomright = self.screen.get_rect().bottomright

        def _move_to_bottomleft_of(self, screen):
            self.rect.bottomleft = self.screen.get_rect().bottomleft

        def blit(self, screen):
            screen.blit(self.img, self.rect)
