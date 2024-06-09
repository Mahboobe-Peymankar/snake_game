from fruit import Fruit

class Pear (Fruit) :
    def __init__(self, width, height):
        super().__init__(width, height,"pictures\pear.png")
        self.score = 2