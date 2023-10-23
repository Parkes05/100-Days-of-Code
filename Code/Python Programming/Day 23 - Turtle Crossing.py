import sys
sys.path.append('../Data')

from turtle import Screen
import time
from crossing_class_23 import *

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.player_move, 'Up')

loop_count = 6
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()

    if player.finish_line():
        player.starting_position()
        scoreboard.update_level()
        print(len(car_manager.all_cars))
        car_manager.higher_car_level()

    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()