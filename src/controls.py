from src.state import State

class Controls():
    def __init__(self):
        self.keyboard = {'right': False,
                         'left': False, }

    def __str__(self):
        return str(self.keyboard)

    def right_down(self):
        self.keyboard["right"] = True

    def left_down(self):
        self.keyboard["left"] = True

    def right_up(self):
        self.keyboard["right"] = False

    def left_up(self):
        self.keyboard["left"] = False

    def what_fish_should_do(self):
        if self.keyboard['right'] and not self.keyboard['left']:
            return State.right
        elif self.keyboard['left'] and not self.keyboard['right']:
            return State.left
        elif self.keyboard['left'] and self.keyboard['right']:
            return State.stop
        else:
            return State.stop
