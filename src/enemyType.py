class EnemyType():
    def __init__(self, speed, width, height,path_R, path_S, path_L, hitbox_offset_and_size=[0,0,10,10]):
        self.speed = speed
        self.width = width
        self.height = height
        self.size = [width, height]
        self.img_path_R = path_R
        self.img_path_S = path_S
        self.img_path_L = path_L

        self.hitbox_offset_and_size=hitbox_offset_and_size