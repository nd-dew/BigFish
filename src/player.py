import pygame

class Player():
    def __init__(self):
        self.color=(255,255,255) # R G B
        self.position=[300, 500] # x,y
        self.size=[30, 30] # width, height

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.position + self.size )  # rect: (x1, y1, width, height)

    def move_player(self, xy_transition):
        """ :param xy_transition: should be a 2 element list [x_move, y_move]
        """
        self.position = [ self.position[0] + xy_transition [0] , self.position[1] + xy_transition [1] ]

    def check_keys_and_move(self):
        keys = pygame.key.get_pressed()  # checking pressed key
        if keys[pygame.K_LEFT]:
            x_transition = -1
            self.move_player([x_transition, 0])
        elif keys[pygame.K_RIGHT]:
            x_transition =  1
            self.move_player([x_transition, 0])
