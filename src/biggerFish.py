import random
import pygame
from src import settings
from src import player
from src import enemy
from src.state import State
from src.controls import Controls
import logging
import time

logging.basicConfig(filename='resources/logs/timeOfOneLoop.log', level=logging.INFO)

class BiggerFish:
    def __init__(self):
        pygame.init()
        self.settings = settings.Settings()

        pygame.display.set_caption('Bigger Fish')
        icon = pygame.image.load(self.settings.logo_path)
        pygame.display.set_icon(icon)
        self.screen = pygame.display.set_mode(self.settings.screen_size)  # screen is a tuple of width and height

        # Background
        self.current_bg_animation = 0
        self.bg_surface = self.settings.bg_animation[self.current_bg_animation]
        #self.bg_surface = pygame.transform.scale(self.bg_surface, self.settings.screen_size)

        #self.fog = pygame.image.load('resources/images/fog2.png')
        #self.fog_counter = 0

        # Time variable
        self.clock = pygame.time.Clock()  # for frames per second/ delay?

        # Events ID generator, created to keep track of eventID
        # user event ID has to be between pygame.USEREVENT and pygame.NUMEVENTS
        self.event_id_generator= (id for id in range(pygame.USEREVENT+1, pygame.NUMEVENTS))

        # Counter initialization
        self.counter = self.Counter(self.screen)
        self.counter.addEvent(self.event_id_generator, 100)

        self.enemies = [] # array of enemies
        self.spawn_rate = 500 # initial spawn rate
        self.SPAWN_EVENT = pygame.USEREVENT # TODO use generator in here 'next( self.event_id_generator)'
        pygame.time.set_timer(self.SPAWN_EVENT, self.spawn_rate)

        self.player = player.Player(self)  # pplayer1layer instance
        self.running = True

        self.controls= Controls()

        # Printing things nicely in console
        self.print_buffer=''


    def run_game(self, check_performance=False):
        while self.running:  # Start of the game's main loop
            self.check_events()  # Event loop

            self.player.update()
            # self.player.update(self.controls.what_fish_should_do())  # Checking the update method in PLAYER each loop.
            for enem in self.enemies: # Can be reduced with sprite.group
                enem.update()
            for enem in self.enemies.copy(): # deleting enemies
                if enem.rect.midbottom[1] >= self.settings.screen_height + 50:
                    self.enemies.remove(enem)
            #print('\n',len(self.enemies), end='  ') # checking the size of the list


            self.screen_update()  # Updating screen TODO name is a little confusing it does more like a reneder/blit

            #self.start_time = pygame.time.get_ticks()
            # self.spawn()
            #print(self.controls) # DEBUG


            # PERFORMANCE, Don't limit frames if checking performance
            if check_performance:
                self._check_performance()
            else:
                self.clock.tick(self.settings.FPS)


    # def spawn(self):
    #     if self.start_time > self.spawn_rate:
    #         self.enemies.append(enemy.Enemy(self))
    def spawn_enemies(self):
        self.enemies.append(enemy.Enemy(self))  # adding enemies

    def check_events(self):
        for event in pygame.event.get():
            
            # QUIT GAME
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                self.running = False

            # KEYBOARD INPUT
            elif event.type == pygame.KEYDOWN:  # Check for events when a keypress is done
                if event.key == pygame.K_RIGHT:
                    # self.player.direction = "right"
                    # self.controls.right_down()
                    self.player.right = True
                elif event.key == pygame.K_LEFT:
                    # self.player.direction = "left"
                    # self.controls.left_down()
                    self.player.left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # self.player.direction = "stop"
                    # self.controls.right_up()
                    self.player.right = False
                elif event.key == pygame.K_LEFT:
                    # self.player.direction = "stop"
                    # self.controls.left_up()
                    self.player.left = False

            elif event.type == self.counter.event:
                # increment counter up to 200
                self.counter.update( (self.counter.points + 1)%200 )

            if event.type == self.SPAWN_EVENT: # TODO change to elif
                self.spawn_enemies()

    def screen_update(self):
        self.screen.fill(self.settings.bg_color)  # Redrawing the background each pass

        self.current_bg_animation += 0.5
        if self.current_bg_animation >= len(self.settings.bg_animation):
            self.current_bg_animation = 0
        self.bg_surface = self.settings.bg_animation[int(self.current_bg_animation)]
        self.screen.blit(self.bg_surface, [0, 0])

        # Draw enemies in the screen (iterate over the list of enemies)
        for enem in self.enemies: # Can be reduced with sprite.group
            enem.blit_enemy()

        # Draw player on the screen
        self.player.blit_player(bbox=True)  # drawing our fish on top of our background

        self.counter.blit(self.screen)

        #self.fog_counter -= 1
        #self.screen.blit(self.fog, [self.fog_counter, self.fog_counter])

        pygame.display.flip()  # TODO change to update

    class Counter():
        def __init__(self, parentScreen):
            self.screen = parentScreen
            self.points=0
            self.font = pygame.font.SysFont('Comic Sans MS', 30)
            self.font_color= pygame.Color('white')
            self.img= self.font.render(str(self.points), False,  self.font_color, None)
            self.rect = self.img.get_rect()

            self._move_to_bottomright_of(self.screen)

        def addEvent(self, generator, timeBetweenEvents):
            """ add test event to increment counter every x miliseconds
            """
            self.event=next(generator)
            pygame.time.set_timer(self.event, timeBetweenEvents)

        def eventAction(self):
            self.points = ( self.points + 13 + 100) % 100

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



    def _check_performance(self, num_of_frame_to_average=3000, printing=True, log=True):
        """
        Run in main loop without FPS limitations.

        Parameters
        ----------
        num_of_frame_to_average : int, optional, default 3000
            The more the more accurate calculations are, but you will wait longer for the results.
        printing : bool, optional, default True
            do you want to see results in console
        log : bool, optional, default True
            do you want to output results to log file
        """

        if not hasattr(self,  'loopNumber'):
            # setattr(self._check_performance, 'loopNumber', 0)
            self.loopNumber = 0
            self.start=0
        else:
            if self.loopNumber == 0:
                self.start = time.time()

            self.loopNumber += 1
            if self.loopNumber > num_of_frame_to_average:
                end = time.time()
                one_loop_time = (end - self.start) / self.loopNumber
                if printing:
                    print(f'{one_loop_time=: .6f} s {(1 / one_loop_time): .1f} FPS possible')
                if log:
                    logging.info(f'{one_loop_time=: .6f} s {(1 / one_loop_time): .1f} FPS possible')
                self.loopNumber = 0
