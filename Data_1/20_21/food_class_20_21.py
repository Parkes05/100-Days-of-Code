from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.25)
        self.color('blue')
        self.speed(0)
        self.new_food()
    
    def new_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.setposition(x=random_x, y=random_y)
    
