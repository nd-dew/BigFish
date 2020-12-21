from src.state import State
from enum import Enum


class Controls():
    """
     Attributes
    ----------
    right : bool
        current state of right arrow key True if pressed
    left : bool
        current state of left arrow key True if pressed
    """

    def __init__(self):
        self.right = False
        self.left = False

        #self.stop_ = 1
        #self.left_ = 2
        #self.right_ = 3

    def __str__(self):
        return f'right={self.right}, left={self.left}'

    def right_down(self):
        self.right = True

    def left_down(self):
        self.left = True

    def right_up(self):
        self.right = False

    def left_up(self):
        self.left = False

    def what_fish_should_do(self):
        """
        Analyses keyboard state and returns state in which player fish should be
        
        Returns
        -------
        state : State(Enum) What player should do based on keyboard input
        """

        # Pressed right only
        if self.right and not self.left:
            return State.right

        # Pressed left only
        elif self.left and not self.right:
            return State.left

        # Pressed both keys
        elif self.left and self.right:
            return State.stop

        # Nothing pressed
        else:
            return State.stop
