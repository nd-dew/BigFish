import pygame as pg
from src import settings
from src import player
from src import enemy
import logging
import time

logging.basicConfig(filename='resources/logs/timeOfOneLoop.log', level=logging.INFO)


class BiggerFish:
    """
    BiggerFish class is a class thanks to which game instance can be created. It contains, unifies and creates
    the instances of classes found in all of the game files (enemy.py, settings.py, player.py).
    It runs the game in a loop and makes use of different classes to setup the game (Settings Class),
    create the player (Player Class) and the enemies as well (Enemy Class). Also, this class handles events triggered by
    different conditions (for example when keyboard keys are pressed or when some timers get activated).

    Attributes
    ----------
    settings : Settings class
        settings attributes imported as an instance of Settings class
    screen : (int, int)
        game window size
    icon : Pygame image
        icon image for the game window
    clock : Pygame time clock
        clock instance to track time
    event_id_generator : list
        for tracking event ids
    manager : SceneManager class
        SceneManager instance for scenes control
    running : boolean
        True when game is set tu run
    """
    def __init__(self):
        pg.init()
        pg.mixer.init() # initializing the mixer module necessary for music introduction
        self.settings = settings.Settings() # creating a settings instance
        self.screen = pg.display.set_mode(self.settings.screen_size)  # initializing a window for display (screen_size is a tuple of width and height)
        pg.display.set_caption('Bigger Fish') # setting caption
        icon = pg.image.load(self.settings.logo_path) # loading icon image
        pg.display.set_icon(icon)

        # Time variable
        self.clock = pg.time.Clock()  # creating an object to track time

        # Events ID generator, created to keep track of eventID
        # user event ID has to be between pg.USEREVENT and pg.NUMEVENTS
        self.event_id_generator = (id for id in range(pg.USEREVENT + 1, pg.NUMEVENTS))

        # Scenes MANAGER
        self.manager = SceneManager(self) # initiliazing scene manager instance, that changes between main menu, game and game over scene

        # Setting the boolean that handles the running of the game and the loop inside the main menu
        self.running = True  # loop inside game

    def run_game(self, check_performance=False):
        """
        The run_game method uses an instance of SceneManager class that helps managing transitions between scenes.
        One scene class was created for each of the three scenes necessary: MenuScene, GameScene and GameOver.

        Parameters
        ----------
        check_performance : boolean
        """
        while self.running:  # Start of the game's main loop

            self.manager.scene.handle_events()
            self.manager.scene.update()
            self.manager.scene.render(self.screen) # rendering into the screen
            pg.display.flip() # displaying into the screen

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
    This class is used to change scenes and hold currently used.
    Attributes
    ----------
    scene : Scene
        currently displayed scene
    """

    def __init__(self, biggerFish):
        self.go_to(MenuScene(biggerFish))

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self

class Scene():
    """
    This is parent class for all scenes. All scenes has to inherit Scene() class
    The instances of a Scene class are used as a general variable for SceneManager.

    NOTE: External modification: Each Scene gets one attribute externaly via SceneManager/go_to method
    it allows to access manager methods to change current scene:

    Non standard Parameters:
    ----------
    manager: SceneManager, added externally, more info in SceneManager.go_to method

    """
    def handle_events(self):
        """
        Method required in all scenes, it is supposed to detect all the pygame events and take
        actions accordingly.
        """
        pass

    def update(self):
        """
        Method required in all scenes, it performs std update actions on corresponding scene objects.
        """
        pass

    def render(self, screen):
        """
        Method required in all scenes, perform all blit action to the pygame graphical buffer.
        """
        pass

    def display_text(self, screen, text, font_size, x_pos, y_pos):
        """
        This method is used to blit text on the screen at choosen postion
        Parameters
        ----------
        screen : pygame.surface,
            surface to blit onto
        text :  str,
            characters to be blitted
        font_size : int,
            size of the font
        x_pos : int,
            x position on the surface (lefttop corner)
        y_pos : int,
            y position on the surface (lefttop corner)
        """
        font = pg.font.Font(pg.font.match_font('impact'), font_size)
        text_img = font.render(text, True, (0, 0, 0))
        text_rect = text_img.get_rect()
        text_rect.midtop = (x_pos, y_pos)
        screen.blit(text_img, text_rect)

    def read_highscore(self):
        """
        Function provides std way of reading logged highscore
        Returns
        -------
        previous_score : int
            logged highscore
        """
        with open("resources/logs/score", 'r') as f:
            previous_score = int(f.readline())
        return previous_score


class MenuScene(Scene):
    """
    Initial scene of the main menu with the highest score displayed, video animation and music.
    Attributes
    ----------
    biggerFish : biggerFish class,
        instance of the game class to use setting
    music : Pygame mixer music
        chosen music played in mp3
    main_menu_animation : list
        list of images creating an animation
    current_main_menu_animation : Pygame image
        current animation image
    score : int
        current highest score loaded from text file
    """

    def __init__(self, biggerFish):
        # Load music and play it in a loop
        self.biggerFish = biggerFish
        self.music = pg.mixer.music.load("resources/music/casimps1_-_Fishes_in_the_Sea.mp3")
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
        self.score = self.read_highscore()

    def handle_events(self):
        """
            Method checking for the events and executing task based on these events.
            While pressing certain keys, game running can be set to False; GameScene can be change to start the actual
            GameScene; or Debug window can be initiated.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.biggerFish.running = False

            elif event.type == pg.KEYDOWN:  # Change Scene to Game if enter is pressed
                if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                    self.manager.go_to(GameScene(self.biggerFish))

                if event.key == pg.K_F12:
                    self.manager.go_to(DebugHitboxScene(self.biggerFish))

    def update(self):
        """
        Method updating background main menu animation.
        """
        self.current_main_menu_animation += 0.4
        if self.current_main_menu_animation >= len(self.main_menu_animation):
            self.current_main_menu_animation = 0
        self.main_menu_surface = self.main_menu_animation[int(self.current_main_menu_animation)]

    def render(self, screen):
        """
        Method rendering graphical representation of the background animations and the score text field into the
        game window.

        Parameters
        ----------
        screen : Pygame image
        """
        screen.blit(self.main_menu_surface, [0, 0])
        screen.blit(self.main_menu_text, [0, 0])
        self.display_text(screen, str(self.score), 20, 470, 10)


class GameScene(Scene):
    """
    Main game scene handling the player instance, keeping a list of enemies created, spawning of enemies, checking
    the key press events, updating the positions of elements, collisions, score counter, rendering and displaying
    of the elements into the game window.
    Attributes
    ----------
    biggerFish : biggerFish class,
        instance of the game class to use setting
    score :  int,
        current score
    player : Player class,
        instance of the Player class to use its properties
    enemies : list,
        list of currently displayed enemies
    spawn_rate : int,
        spawn rate of the enemy, in ms
    SPAWN_EVENT: int
        generated event id
    current_bg_animation: int
        holds currently displayed bg image
    bg_surface: pygame.surface
        holds currently displayed surface
    sound_game_over : pg.mixer.Sound
        object to hold game over sound
    sound_bite : pg.mixer.Sound
        object to hold bite sound
    sound_enemy : pg.mixer.Sound
        object to hold enemy sound
    sound_start : pg.mixer.Sound
        object to hold start game sound
    """
    def __init__(self, biggerFish):
        self.biggerFish = biggerFish
        self.score = 0
        self.player = player.Player(self.biggerFish)  # player1 instance
        self.enemies = []  # list of enemies
        self.spawn_rate = 300  # initial spawn rate

        # Create Spawn event, keep its id to recognize it
        self.SPAWN_EVENT = next(self.biggerFish.event_id_generator)
        pg.time.set_timer(self.SPAWN_EVENT, self.spawn_rate)

        # Load Background
        self.current_bg_animation = 0
        self.bg_surface = self.biggerFish.settings.bg_animation[self.current_bg_animation]

        # Load music and sounds
        self.sound_game_over = pg.mixer.Sound('resources/music/game_over.mp3')
        self.sound_bite = pg.mixer.Sound('resources/music/bite0.mp3')
        self.sound_enemy = pg.mixer.Sound('resources/music/enemy_bite.mp3')
        self.sound_start = pg.mixer.Sound('resources/music/start.mp3')

        # Play bg music
        self.sound_start.play()

    def handle_events(self):
        """
            Method checking for the events and executing task based on these events.
            While pressing certain keys, game running can be set to False; movement of the player fish can be changed;
            or random enemies spawning can be initiated.
        """
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
        """
        Method updates for player update method to change its position based on events; similarly calls an update
        method of the Enemy class for each of the enemy in the list of active enemies; list of enemies is also
        regularly checked and non-active enemies are deleted. Updated method also call of the collision helper method
        to identify collisions between player and enemies.
        """
        self.player.update(self.score)
        for enem in self.enemies:
            enem.update()
        for enem in self.enemies.copy():  # deleting enemies
            if enem.rect.midbottom[1] >= self.biggerFish.settings.screen_height + 150:
                self.enemies.remove(enem)
        self._collision_general()

    def render(self, screen):  # It should take screen to render things
        """
        Method taking care of the graphical rendering of the animations into the background, each of the enemies (with
        hitbox rectangles if desired) and the player (with hitbox rectangle if desired) into the game window.
        Additional score text field is displayed on top as well.

        Parameters
        ----------
        screen : Pygame image
            updating game screen
        """
        screen.fill(self.biggerFish.settings.bg_color)  # Redrawing the background each pass
        self.current_bg_animation += 0.5
        if self.current_bg_animation >= len(self.biggerFish.settings.bg_animation):
            self.current_bg_animation = 0
        self.bg_surface = self.biggerFish.settings.bg_animation[int(self.current_bg_animation)]
        screen.blit(self.bg_surface, [0, 0])

        # Draw enemies in the screen (iterate over the list of enemies)
        for enem in self.enemies:
            enem.blit_enemy(bbox=False, hitbox=False)

        # Draw player on the screen
        self.player.blit_player(bbox=False, hitbox=False)  # drawing our fish on top of our background
        # Draw score
        screen.blit(self.biggerFish.settings.score_text, [0, 0])
        self.display_text(screen, str(self.score), 20, 470, 10)

    def _spawn_enemies(self):
        """
        Method appending the list of enemies while reating the new instances of the Enemy class.
        """
        self.enemies.append(enemy.Enemy(self.biggerFish))  # adding enemies

    def _collision_general(self):
        """
        helper method to identify whether two objects in the game collided.
        """
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
                        self.score += 1
                    # GAME OVER
                    else:
                        self._save_score()
                        self.manager.go_to(GameOver(self.biggerFish))

    def _display_text(self, screen, text, font_size, x_pos, y_pos):
        """
        This method is used to blit text on the screen at choosen postion
        Parameters
        ----------
        screen : pygame.surface,
            surface to blit onto
        text :  str,
            characters to be blitted
        font_size : int,
            size of the font
        x_pos : int,
            x position on the surface (lefttop corner)
        y_pos : int,
            y position on the surface (lefttop corner)
        """
        font = pg.font.Font(pg.font.match_font('impact'), font_size)
        text_img = font.render(text, True, (0, 0, 0))
        text_rect = text_img.get_rect()
        text_rect.midtop = (x_pos, y_pos)
        screen.blit(text_img, text_rect)

    def _save_score(self):
        """
        Save score to file if it is high enough.
        """
        previous_score = self.read_highscore()

        if self.score > previous_score:
            with open("resources/logs/score", 'w') as f:
                f.write(str(self.score) + '\n')


class GameOver(Scene):
    """
    Scene that is called when the player is dead and can return to MenuScene or end the game.
    """
    def __init__(self, biggerFish):
        self.biggerFish = biggerFish

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

    def render(self, screen):  # It sould take screen to render things
        screen.blit(self.biggerFish.settings.game_over_img, [0, 0])


class DebugHitboxScene(Scene):
    """
    Scene to see all of the bounding boxes, and hitboxes of all enemies and all players (there is one
    player but it has multiple versions/levels)
    It can be accesed with F12 key in main menu, and left with pressing enter, arrow keys will change
    player level.

    Attributes
    ----------
    biggerFish : BiggerFish class
    score : int
    generated_artificial_enemies : list
        list of artificial enemies for debug purposes
    player : Player class
        player class instance
    """

    def __init__(self, biggerFish):
        self.biggerFish = biggerFish

        self.score = 0

        self.generated_artificial_enemies = []
        previous_rect = pg.Rect(0, 0, 40, 3)
        previous_rect.topleft = self.biggerFish.screen.get_rect().topleft
        for i in range(len(self.biggerFish.settings.enemies)):
            e = enemy.Enemy(self.biggerFish, custom_index=i)
            e.rect.topleft = previous_rect.topright
            e.rect.x += 1
            if e.rect.right > self.biggerFish.screen.get_rect().right:
                e.rect.x = 0
                e.rect.y = e.rect.y + 130
            if i == 14:
                e.rect.y = e.rect.y + 35
            previous_rect = e.rect
            self.generated_artificial_enemies.append(e)
        self.player = player.Player(self.biggerFish)

    def handle_events(self):
        """
            Method checking for the events and executing task based on these events.
            While pressing certain keys, game running can be set to False; manual adding of score.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.biggerFish.running = False

            elif event.type == pg.KEYDOWN:  # Change Scene to Game if enter is pressed
                if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                    self.manager.go_to(MenuScene(self.biggerFish))

                if event.key == pg.K_UP:
                    self.score += 1

                if event.key == pg.K_DOWN:
                    self.score -= 1

    def update(self):
        for r in self.generated_artificial_enemies:
            r.update(debugMode=True)
        self.player.update(self.score)

    def render(self, screen):
        """
        Rendering screen image, artificial enemies with hitboxes rectangles, game clock, player surface and score
        text field into the game window.

        Parameters
        ----------
        screen : pygame image
        """
        previous_rect = pg.Rect(0, 0, 40, 3)
        previous_rect.topleft = screen.get_rect().topleft
        screen.fill((0, 0, 255))
        for r in self.generated_artificial_enemies:
            r.blit_enemy(bbox=True, hitbox=True)
        self.player.blit_player(bbox=True, hitbox=True)
        self.biggerFish.clock.tick(30)

        self.display_text(screen, str(self.score), 20, 470, 100)
