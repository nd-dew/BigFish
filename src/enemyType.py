class EnemyType():
    """
    This class regroups all the attributes that differ for each of the enemy type.

    Attributes
    ----------
    speed : int
        speed of the enemy
    width : int
        width of the enemy image
    height : int
        width of the enemu image
    size : [int, int]
        [width, height]
    img_path_R : String
        path to the image with right curved tail of the enemy
    img_path_S : String
        path to the image with steady tail of the enemy
    img_path_L : String
        path to the image with left curved tail of the enemy
    hitbox_offset_and_size : [int, int, int, int]
        specifying the offset from the image size where the collisions are occuring
    """
    def __init__(self, speed, width, height,path_R, path_S, path_L, hitbox_offset_and_size=[0,0,10,10]):
        self.speed = speed
        self.width = width
        self.height = height
        self.size = [width, height]
        # Paths to sprite images (image with right tail, tail steady, or left tail)
        self.img_path_R = path_R
        self.img_path_S = path_S
        self.img_path_L = path_L
        # hitbox offset and size is used to specify the area that will be engaged in collisions
        self.hitbox_offset_and_size = hitbox_offset_and_size