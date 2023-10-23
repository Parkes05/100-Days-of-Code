from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
FONT = ("Courier", 24, "normal")
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class CarManager():
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.all_cars = []
    
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape('square')
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.setheading(180)
            car.setposition(300, random.randint(-250, 250))
            self.all_cars.append(car)

    def car_move(self):
        for cars in self.all_cars:
            cars.forward(self.move_distance)

    def higher_car_level(self):
        self.move_distance += MOVE_INCREMENT
        for cars in self.all_cars:
            cars.hideturtle()
        self.all_cars = []

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.starting_position()
    
    def player_move(self):
        self.forward(MOVE_DISTANCE)
    
    def finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False
    
    def starting_position(self):
        self.setposition(STARTING_POSITION)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 1
        self.hideturtle()
        self.penup()
        self.setposition(-280, 250)
        self.score()

    def score(self):
        self.write(arg=f'Level: {self.player_score}', align='left', font=FONT)    
    
    def update_level(self):
        self.player_score += 1
        self.clear()
        self.score()
    
    def game_over(self):
        self.home()
        self.write(arg=f'GAME OVER', align='center', font=FONT)    
