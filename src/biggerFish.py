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
        pg.mixer.init()
        self.settings = settings.Settings()
        self.screen = pg.display.set_mode(self.settings.screen_size)  # screen is a tuple of width and height
        pg.display.set_caption('Bigger Fish')
        icon = pg.image.load(self.settings.logo_path)
        pg.display.set_icon(icon)

        # Time variable
        self.clock = pg.time.Clock()  # for frames per second/ delay?

        # Events ID generator, created to keep track of eventID
        # user event ID has to be between pg.USEREVENT and pg.NUMEVENTS
        self.event_id_generator = (id for id in range(pg.USEREVENT + 1, pg.NUMEVENTS))


        # Setting the boolean that handles the running of the game and the loop inside the main menu
        self.running = True #loop inside game

        # Scenes MANAGER
        self.manager= SceneManager(self)

    def run_game(self, check_performance=False):
        while self.running:  # Start of the game's main loop

            self.manager.scene.handle_events()
            self.manager.scene.update()
            self.manager.scene.render(self.screen)
            pg.display.flip() # TODO Maybe place it inside scene???? with decorators

            # PERFORMANCE, Don't limit frames if checking performance
            if check_performance:
                self._check_performance()
            else:
                self.clock.tick(self.settings.FPS)


    def _check_performance(self, num_of_frame_to_average=100, printing=True, log=True):
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

        if not hasattr(self, 'loopNumber'):
            # setattr(self._check_performance, 'loopNumber', 0)
            self.loopNumber = 0
            self.start = 0
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
                    logging.info('{one_loop_time=: .6f} s {(1 / one_loop_time): .1f} FPS possible')
                self.loopNumber = 0

class SceneManager():
    """
    This class is uded to change scenes and hold currently used.
    """
    def __init__(self, biggerFish):
        self.biggerFish= biggerFish
        self.go_to(MenuScene(biggerFish))
        self.mama="go daddy go"

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self


class Scene():
    # def __init__(self, biggerFish):
    #     self.biggerFish = biggerFish

    def handle_events(self):
       pass

    def update(self):
        pass

    def render(self, screen): # It sould take screen to render things
        pass

    def display_text(self, screen, text, font_size, x_pos, y_pos):
        font = pg.font.Font(pg.font.match_font('impact'), font_size)
        text_img = font.render(text, True, (0, 0, 0))
        text_rect = text_img.get_rect()
        text_rect.midtop = (x_pos, y_pos)
        screen.blit(text_img, text_rect)

    def read_highscore(self):
        with open("resources/logs/score", 'r') as f:
            previous_score= int(f.readline())
        return previous_score

class MenuScene(Scene):

    def __init__(self, biggerFish):
        # Load music and play it in a loop
        self.biggerFish=biggerFish
        self.music= pg.mixer.music.load("resources/music/casimps1_-_Fishes_in_the_Sea.mp3")
        pg.mixer.music.play(-1)
        # Load BG animations
        self.main_menu_animation = []
        for j in range(0, 28):
            string2 = 'resources/images/main_menu/main_menu_' + str(j) + '.png'
            self.main_menu_animation.append(pg.image.load(string2))

        # Set first bg image in sequence as current
        self.current_main_menu_animation = 0
        self.main_menu_surface = self.main_menu_animation[self.current_main_menu_animation]

        # Load Title displayed over BG
        self.main_menu_text = pg.image.load("resources/images/main_menu/all_menu.png")

        # Read max score from file
        self.score=self.read_highscore()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.biggerFish.running = False

            elif event.type == pg.KEYDOWN:  # Change Scene to Game if enter is pressed
                if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                    self.manager.go_to(GameScene(self.biggerFish))

                if event.key == pg.K_F12:
                    self.manager.go_to(DebugHitboxScene(self.biggerFish))


    def update(self):
        self.current_main_menu_animation += 0.4
        if self.current_main_menu_animation >= len(self.main_menu_animation):
            self.current_main_menu_animation = 0
        self.main_menu_surface = self.main_menu_animation[int(self.current_main_menu_animation)]

    def render(self, screen): # It sould take screen to render things
        screen.blit(self.main_menu_surface, [0, 0])
        screen.blit(self.main_menu_text, [0,0])
        self.display_text(screen, str(self.score), 20, 470, 10)


class GameScene(Scene):
    def __init__(self, biggerFish):
        self.biggerFish = biggerFish
        self.score = 0
        self.player = player.Player(self.biggerFish)  # player1 instance
        self.enemies = []  # array of enemies
        self.spawn_rate = 300  # initial spawn rate

        #Create Spawn event, keep its id to recognize it
        self.SPAWN_EVENT = next(self.biggerFish.event_id_generator)
        pg.time.set_timer(self.SPAWN_EVENT, self.spawn_rate)

        # Load Background
        self.current_bg_animation = 0
        self.bg_surface = self.biggerFish.settings.bg_animation[self.current_bg_animation]

        # Load music and sounds
        self.sound_game_over = pg.mixer.Sound('resources/music/game_over.mp3')
        self.sound_bite = pg.mixer.Sound('resources/music/bite0.mp3')
        self.sound_enemy = pg.mixer.Sound('resources/music/enemy_bite.mp3')
        self.sound_start = pg.mixer.Sound('resources/music/start.mp3') # TODO music should be MUSIC object not Sound

        # Play bg music
        self.sound_start.play()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.biggerFish.running = False

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

            elif event.type == self.SPAWN_EVENT:
                self._spawn_enemies()

    def update(self):
        self.player.update()
        for enem in self.enemies:  # Can be reduced with sprite.group
            enem.update()
        for enem in self.enemies.copy():  # deleting enemies
            if enem.rect.midbottom[1] >= self.biggerFish.settings.screen_height + 150:
                self.enemies.remove(enem)
        self._collision_general()



    def render(self, screen):  # It sould take screen to render things
        screen.fill(self.biggerFish.settings.bg_color)  # Redrawing the background each pass
        self.current_bg_animation += 0.5
        if self.current_bg_animation >= len(self.biggerFish.settings.bg_animation):
             self.current_bg_animation = 0
        self.bg_surface = self.biggerFish.settings.bg_animation[int(self.current_bg_animation)]
        screen.blit(self.bg_surface, [0, 0])

        # Draw enemies in the screen (iterate over the list of enemies)
        for enem in self.enemies:  # Can be reduced with sprite.group
            enem.blit_enemy(bbox=False, hitbox=True)

        # Draw player on the screen
        self.player.blit_player(bbox=False, hitbox=True)  # drawing our fish on top of our background
        #
        # Draw score
        screen.blit(self.biggerFish.settings.score_text, [0, 0])
        self.display_text(screen, str(self.score), 20, 470, 10)

    def _spawn_enemies(self):
        self.enemies.append(enemy.Enemy(self.biggerFish))  # adding enemies

    def _collision_general(self):
        for enemy in self.enemies:
            # If hitboxes rects are collided
            if self.player.hitbox.colliderect(enemy.hitbox):  # if two rectangles overlap
                # If they are kissing in head
                if enemy.hitbox.bottom < self.player.hitbox.top + 10:
                    # If player is thicker
                    if enemy.hitbox.w < self.player.hitbox.w:
                        self.sound_bite.play()
                        self.enemies.remove(enemy)
                        # self.counter.add_points(1)
                        self.score+=1
                    # GAME OVER
                    else:
                        self._save_score()
                        self.manager.go_to(GameOver(self.biggerFish))

    def _display_text(self, screen, text, font_size, x_pos, y_pos):
        font = pg.font.Font(pg.font.match_font('impact'), font_size)
        text_img = font.render(text, True, (0, 0, 0))
        text_rect = text_img.get_rect()
        text_rect.midtop = (x_pos, y_pos)
        screen.blit(text_img, text_rect)

    def _save_score(self):
        """
        Save score to file if it is high enough.
        """
        previous_score= self.read_highscore()

        if self.score > previous_score:
            with open("resources/logs/score", 'w') as f:
                f.write(str(self.score) + '\n')

class GameOver(Scene):

    def __init__(self, biggerFish):
        self.biggerFish=biggerFish

        # Load music and play it
        pg.mixer.music.stop()
        self.sound_enemy = pg.mixer.Sound('resources/music/enemy_bite.mp3')
        self.sound_game_over = pg.mixer.Sound('resources/music/game_over.mp3')
        self.sound_enemy.play()
        self.sound_game_over.play()


    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.biggerFish.running = False

            elif event.type == pg.KEYDOWN:  # Change Scene to Game if enter is pressed
                if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                    self.manager.go_to(MenuScene(self.biggerFish))


    def render(self, screen): # It sould take screen to render things
        screen.blit(self.biggerFish.settings.game_over_img, [0, 0])

class DebugHitboxScene(Scene):

    def __init__(self, biggerFish):
        self.biggerFish=biggerFish
        
        self.generated_artificial_enemies=[]
        previous_rect = pg.Rect(0, 0, 40, 3)
        previous_rect.topleft =  self.biggerFish.screen.get_rect().topleft
        for i in range(len(self.biggerFish.settings.enemies)):
            e = enemy.Enemy(self.biggerFish, custom_index=i)
            e.rect.topleft = previous_rect.topright
            e.rect.x+=1
            if e.rect.right >  self.biggerFish.screen.get_rect().right:
                e.rect.x = 0
                e.rect.y = e.rect.y + 120
            previous_rect = e.rect
            self.generated_artificial_enemies.append(e)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.biggerFish.running = False

            elif event.type == pg.KEYDOWN:  # Change Scene to Game if enter is pressed
                if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                    self.manager.go_to(MenuScene(self.biggerFish))

    def update(self):
        for r in self.generated_artificial_enemies:
            r.update(debugMode=True)

    def render(self, screen): # It sould take screen to render things
        previous_rect=pg.Rect(0,0,40,3)
        previous_rect.topleft=screen.get_rect().topleft
        screen.fill((0, 0, 255))
        e = enemy.Enemy(self.biggerFish, custom_index=1)
        e.rect.midbottom= screen.get_rect().midbottom
        # e.hitbox=e.rect
        e.blit_enemy(bbox=False, hitbox=True)
        for r in self.generated_artificial_enemies:
            r.blit_enemy(bbox=True, hitbox=True)
