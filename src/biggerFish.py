import pygame as pg
from src import settings
from src import player
from src import enemy
import logging
import time

logging.basicConfig(filename='resources/logs/timeOfOneLoop.log', level=logging.INFO)

class BiggerFish:
    def __init__(self):
        pg.init()
        self.settings = settings.Settings()
        self.screen = pg.display.set_mode(self.settings.screen_size)  # screen is a tuple of width and height
        pg.display.set_caption('Bigger Fish')
        icon = pg.image.load(self.settings.logo_path)
        pg.display.set_icon(icon)

        # Background
        self.current_bg_animation = 0
        self.bg_surface = self.settings.bg_animation[self.current_bg_animation]

        # Main Menu Background
        self.current_main_menu_animation = 0
        self.main_menu_surface = self.settings.main_menu_animation[self.current_main_menu_animation]

        # Time variable
        self.clock = pg.time.Clock()  # for frames per second/ delay?

        # Events ID generator, created to keep track of eventID
        # user event ID has to be between pg.USEREVENT and pg.NUMEVENTS
        self.event_id_generator = (id for id in range(pg.USEREVENT + 1, pg.NUMEVENTS))
        self.SPAWN_EVENT = pg.USEREVENT  # TODO use generator in here 'next( self.event_id_generator)'

        # Setting the boolean that handles the running of the game and the loop inside the main menu
        self.running = True #loop inside game
        self.loop = False #loop inside main menu
        self.game_over = False #loop inside gameover

        # Printing things nicely in console
        self.print_buffer = ''

        # Initializing background music
        pg.mixer.init()

        # Main menu flag
        self.go_main_menu = True

        # Initializing high score and score
        self.high_score = 0
        self.score = 0

        # SOUND EFFECTS
        self.sound_start = pg.mixer.Sound('resources/music/start.mp3')
        self.sound_game_over = pg.mixer.Sound('resources/music/game_over.mp3')
        self.sound_bite = pg.mixer.Sound('resources/music/bite0.mp3')
        self.sound_enemy = pg.mixer.Sound('resources/music/enemy_bite.mp3')

    def run_game(self, check_performance=False):
        while self.running:  # Start of the game's main loop

            # GAME OVER LOOP FOR A COUPLE OF SECS
            wait = 0
            while self.game_over == True:
                self.screen.blit(self.settings.game_over_img, [0, 0])
                self.clock.tick(60)
                pg.display.flip()
                wait += 1
                if wait > 150: self.game_over = False

            # MAIN MENU HOLDING THE GAME FROM STARTING
            if self.go_main_menu == True:
                self.main_menu_screen() #HERE IS THE INFINITE LOOP METHOD THAT HOLDS THE GAME IN MAIN MENU
                self.go_main_menu = False

                # NEW GAME INITIALIZATION (INITIALIZED VARIABLES LIKE PLAYER, ENEMIES AND SO ON MUST REMAIN HERE)
                self.score = 0
                self.player = player.Player(self)  # player1 instance
                self.enemies = []  # array of enemies
                self.spawn_rate = 300  # initial spawn rate
                pg.time.set_timer(self.SPAWN_EVENT, self.spawn_rate)
                self.sound_start.play()

            self.check_events()  # Event loop
            self.player.update()
            for enem in self.enemies:  # Can be reduced with sprite.group
                enem.update()
            for enem in self.enemies.copy():  # deleting enemies
                if enem.rect.midbottom[1] >= self.settings.screen_height + 150:
                    self.enemies.remove(enem)
            # print('\n',len(self.enemies), end='  ') # checking the size of the list

            self.collision_general()
            self.screen_update()  # Updating screen

            # PERFORMANCE, Don't limit frames if checking performance
            if check_performance:
                self._check_performance()
            else:
                self.clock.tick(self.settings.FPS)

    # Main menu infinite loop until event of pressing ENTER is triggered (changing loop to False)
    def main_menu_screen(self):
        pg.mixer.music.load("resources/music/casimps1_-_Fishes_in_the_Sea.mp3")
        pg.mixer.music.play(1, 0, 0)
        self.loop = True
        while self.loop:
            self.current_main_menu_animation += 0.4
            if self.current_main_menu_animation >= len(self.settings.main_menu_animation):
                self.current_main_menu_animation = 0
            self.main_menu_surface = self.settings.main_menu_animation[int(self.current_main_menu_animation)]
            self.screen.blit(self.main_menu_surface, [0, 0])
            self.screen.blit(self.settings.main_menu_text, [0,0])
            self.display_text(self.screen, str(self.high_score), 20, 470, 10)
            pg.display.flip()
            self.clock.tick(60)
            self.check_events()

    def display_text(self, screen, text, font_size, x_pos, y_pos):
        font = pg.font.Font(pg.font.match_font('impact'), font_size)
        text_img = font.render(text, True, (0, 0, 0))
        text_rect = text_img.get_rect()
        text_rect.midtop = (x_pos, y_pos)
        screen.blit(text_img, text_rect)

    def spawn_enemies(self):
        self.enemies.append(enemy.Enemy(self))  # adding enemies

    def check_events(self):
        for event in pg.event.get():
            # QUIT GAME
            if(self.loop == False):
                if event.type == pg.QUIT or event.type == pg.K_ESCAPE:
                    self.running = False
                # KEYBOARD INPUT
                elif event.type == pg.KEYDOWN:  # Check for events when a keypress is done
                    if event.key == pg.K_RIGHT:
                        self.player.right = True
                    elif event.key == pg.K_LEFT:
                        self.player.left = True
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_RIGHT:
                        self.player.right = False
                    elif event.key == pg.K_LEFT:
                        self.player.left = False
                if event.type == self.SPAWN_EVENT:  # TODO change to elif
                    self.spawn_enemies()
            else:
                if event.type == pg.QUIT or event.type == pg.K_ESCAPE:
                    self.running = False
                # KEYBOARD INPUT
                elif event.type == pg.KEYDOWN:  # Check for events when a keypress is done
                    if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                        self.loop = False

    def screen_update(self):
        self.screen.fill(self.settings.bg_color)  # Redrawing the background each pass
        self.current_bg_animation += 0.5
        if self.current_bg_animation >= len(self.settings.bg_animation):
            self.current_bg_animation = 0
        self.bg_surface = self.settings.bg_animation[int(self.current_bg_animation)]
        self.screen.blit(self.bg_surface, [0, 0])

        # Draw enemies in the screen (iterate over the list of enemies)
        for enem in self.enemies:  # Can be reduced with sprite.group
            enem.blit_enemy(bbox=True, hitbox=True)

        # Draw player on the screen
        self.player.blit_player(bbox=True, hitbox=True)  # drawing our fish on top of our background

        # Draw score
        self.screen.blit(self.settings.score_text, [0, 0])
        self.display_text(self.screen, str(self.score), 20, 470, 10)

        pg.display.flip()  # TODO change to update

    def get_high_score(self):
        return self.high_score
    def set_high_score(self, new_high_score):
        self.high_score = new_high_score
    def get_score(self):
        return self.score
    def increase_score(self, value):
        self.score += value

    def collision_general(self):
        for enemy in self.enemies:
            # If hitboxes rects are collided
            if self.player.hitbox.colliderect(enemy.hitbox): # if two rectangles overlap
                # If they are kissing in head
                if enemy.hitbox.bottom < self.player.hitbox.top + 10:
                    # If player is thicker
                    if enemy.hitbox.w < self.player.hitbox.w:
                        self.sound_bite.play()
                        self.enemies.remove(enemy)
                        #self.counter.add_points(1)
                        self.increase_score(1)
                    # GAME OVER
                    else:
                        self.sound_enemy.play()
                        self.sound_game_over.play()
                        new_score = self.get_score()
                        if new_score > self.get_high_score():
                            self.set_high_score(new_score)
                        pg.mixer.music.stop()
                        self.game_over = True
                        self.go_main_menu = True

    # class Counter:
    #     def __init__(self, parentScreen):
    #         self.screen = parentScreen
    #         self.points = 0
    #         self.font = pg.font.SysFont('Comic Sans MS', 30)
    #         self.font_color = pg.Color('white')
    #         self.img = self.font.render(str(self.points), False, self.font_color, None)
    #         self.rect = self.img.get_rect()
    #
    #         self._move_to_bottomright_of(self.screen)
    #
    #     def addEvent(self, generator, timeBetweenEvents):
    #         """ add test event to increment counter every x miliseconds
    #         """
    #         self.event = next(generator)
    #         pg.time.set_timer(self.event, timeBetweenEvents)
    #
    #     def eventAction(self):
    #         self.points = (self.points + 13 + 100) % 100
    #
    #     def update(self, points=None):
    #         if points != None:
    #             self.points = points
    #         self.img = self.font.render(str(self.points), False, self.font_color, None)
    #         self.rect = self.img.get_rect()
    #         self._move_to_bottomright_of(self.screen)
    #
    #     def _move_to_bottomright_of(self, screen):
    #         self.rect.bottomright = self.screen.get_rect().bottomright
    #
    #     def _move_to_bottomleft_of(self, screen):
    #         self.rect.bottomleft = self.screen.get_rect().bottomleft
    #
    #     def blit(self, screen):
    #         screen.blit(self.img, self.rect)
    #
    #     def add_points(self, points):
    #         self.points += points
    #
    #     def get_points(self):
    #         return self.points

    # def _check_performance(self, num_of_frame_to_average=100, printing=True, log=True):
    #     """
    #     Run in main loop without FPS limitations.
    #
    #     Parameters
    #     ----------
    #     num_of_frame_to_average : int, optional, default 3000
    #         The more the more accurate calculations are, but you will wait longer for the results.
    #     printing : bool, optional, default True
    #         do you want to see results in console
    #     log : bool, optional, default True
    #         do you want to output results to log file
    #     """
    #
    #     if not hasattr(self, 'loopNumber'):
    #         # setattr(self._check_performance, 'loopNumber', 0)
    #         self.loopNumber = 0
    #         self.start = 0
    #     else:
    #         if self.loopNumber == 0:
    #             self.start = time.time()
    #
    #         self.loopNumber += 1
    #         if self.loopNumber > num_of_frame_to_average:
    #             end = time.time()
    #             one_loop_time = (end - self.start) / self.loopNumber
    #             if printing:
    #                 print(f'{one_loop_time=: .6f} s {(1 / one_loop_time): .1f} FPS possible')
    #             if log:
    #                 logging.info('{one_loop_time=: .6f} s {(1 / one_loop_time): .1f} FPS possible')
    #             self.loopNumber = 0