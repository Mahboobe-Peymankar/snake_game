import random

import arcade

from apple import Apple
from pear import Pear
from poo import Poo
from snake import Snake 

# class Apple (arcade.Sprite):
#     def __init__(self,width,height):
#         super().__init__ ("pictures\\apple.png")
#         self.score = 1
#         self.width = 32
#         self.height = 32
#         self.center_x = random.randint (10, width-10)
#         self.center_y = random.randint (10, height-10)
#         self.change_x = 0
#         self.change_y = 0

        

class Game (arcade.Window):
    def __init__(self):
        super().__init__ (width=500 , height= 500 ,title= "supersnake🐍 v1")
        arcade.set_background_color(arcade.color.DARK_KHAKI)
        # self.apple = Apple (self.width , self.height)
        # self.pear = Pear (self.width , self.height)
        # self.poo = Poo (self.width , self.height)
        self.snake = Snake (self)
        self.food_item = []
        self.create_food ()
        self.game_over = False
        self.elapsed_time = 0
        self.time_taken = 0
    
    def create_food (self):
        rand_int = random.randint (1,2)
        
        if rand_int == 1:
            new_food = Apple (self.width , self.height) 
        elif rand_int == 2 :
            new_food = Pear (self.width , self.height) 
        else :
            new_food = Poo (self.width , self.height) 
        
        self.food_item.append (new_food)
        

    def on_draw(self):
        arcade.start_render()
        if self.game_over :
           
          
           arcade.set_background_color (arcade.color.BLACK) 
                    
           arcade.draw_text("Game Over", 150, 250, arcade.color.WHITE, font_size= 20)
           arcade.draw_text(f"Score = {self.snake.score} , time = {int (self.time_taken)}", 150, 200, arcade.color.WHITE, font_size= 10)
           
        else:
            self.snake.draw() 
            for food in self.food_item :
                food.draw ()
            arcade.draw_text (f"Score = {self.snake.score}" , 400 , 10 , color = arcade.color.GRAY , font_size= 10 )
            
            
        arcade.finish_render()

  
    

    def on_update(self, delta_time: float):
       self.time_taken += delta_time
       if  not self.game_over:
            self.elapsed_time += delta_time

            self.snake.change_position (self.food_item[0])

            self.snake.move ()

            if self.elapsed_time > 5  :
                
                self.create_food ()
                self.food_item.remove (self.food_item[0])
                self.elapsed_time = 0

            for food in self.food_item :
                if arcade.check_for_collision (self.snake ,food) :
                        
                    self.snake.eat (food)
                    self.food_item.remove (food)
                        
                    self.create_food ()

            if self.snake.center_x < 0 or self.snake.center_x > self.width or self.snake.center_y < 0 or self.snake.center_y > self.height  :
                self.game_over = True

            if self.snake.score < 0 :
                self.game_over = True

            for body in self.snake.body:
                if self.snake.center_x - body["x"]== 0 and self.snake.center_y - body["y"]== 0:
                    print ("colision")
                    self.game_over =  True
                    break
            



if __name__ == "__main__" :
    game = Game ()
    arcade.run ()