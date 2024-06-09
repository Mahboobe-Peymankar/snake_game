import arcade

class Snake (arcade.Sprite):
    def __init__(self ,game): 
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.color = arcade.color.GREEN
        self.speed = 4
        self.score = 0
        self.body = []
        self.body_color_1 = arcade.color.RED
        self.body_color_2 = arcade.color.YELLOW

    def draw (self):
       
        i = 0
        for part in self.body :
            if i % 2 == 0 :
                arcade.draw_rectangle_filled (part ['x'] , part ['y'] ,self.width , self.height , self.body_color_1)
            else :
                arcade.draw_rectangle_filled (part ['x'] , part ['y'] ,self.width , self.height , self.body_color_2)
            i += 1
        arcade.draw_rectangle_filled (self.center_x,self.center_y , self.width ,self.height,self.color)

    def change_position (self,food) :
        
        if food.score == 2  or food.score == 1:
            if abs (self.center_x - food.center_x) < abs (self.center_y-food.center_y) :
                if self.center_x - food.center_x < 0  :
                    if len (self.body) == 0 :
                        self.change_x = 1
                        self.change_y = 0
                    # else :
                    #     if self.body ['x'] < self.center_x :
                    #         self.change_x = 1
                    #         self.change_y = 0

                else :
                    if len (self.body) == 0 :
                        self.change_x = -1
                        self.change_y = 0
                    # else :
                    #     if self.body ['x'] > self.center_x :
                    #         self.change_x = -1
                    #         self.change_y = 0
            else :
                if self.center_y - food.center_y < 0  :
                    if len (self.body) == 0 :
                        self.change_x = 0
                        self.change_y = 1
                    # else :
                    #     if self.body ['y'] < self.center_y :
                    #         self.change_x = 0
                    #         self.change_y = 1

                else :
                    if len (self.body) == 0 :
                        self.change_x = 0
                        self.change_y = -1
                    # else :
                    #     if self.body ['y'] > self.center_y :
                    #         self.change_x = 0
                    #         self.change_y = -1


    def move (self):
        self.body.append({'x' :self.center_x , 'y' :self.center_y})
        if len (self.body) > self.score :
            self.body.pop(0)
        self.center_x  += self.speed * self.change_x
        self.center_y += self.speed * self.change_y
        
        
    def eat (self,food):
             
        self.score += food.score
        del food
        
        
