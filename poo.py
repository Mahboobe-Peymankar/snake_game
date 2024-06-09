from fruit import Fruit

class Poo (Fruit) :
    def __init__(self, width, height):
        super().__init__(width, height,"pictures\poo.png")
        self.score = -1
