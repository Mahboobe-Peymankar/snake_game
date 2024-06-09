import random
import arcade

class Fruit (arcade.Sprite):
     def __init__(self , width , height , picture):
        super().__init__ (picture)
        self.width = 32
        self.height = 32
        self.center_x = random.randint (10, width-10)
        self.center_y = random.randint (10, height-10)
        self.change_x = 0
        self.change_y = 0
