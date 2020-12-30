class EnemyType():
    def __init__(self, speed, hit_width, hit_ratio, path_R, path_S, path_L):
        self.speed = speed
        self.hit_width = hit_width
        self.width = int(self.hit_width / hit_ratio)
        self.img_path_R = path_R
        self.img_path_S = path_S
        self.img_path_L = path_L

