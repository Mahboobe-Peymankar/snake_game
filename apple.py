from fruit import Fruit

class Apple (Fruit):
    def __init__(self, width, height):
        super().__init__(width, height, "pictures\\apple.png")
        self.score = 1