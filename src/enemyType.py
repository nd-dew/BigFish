class EnemyType():
    def __init__(self, speed, width, path_R, path_S, path_L):
        self.speed = speed
        self.width = width
        # self.height = self.width # squares from now
        # self.size = [self.width, self.height]
        self.img_path_R = path_R
        self.img_path_S = path_S
        self.img_path_L = path_L

