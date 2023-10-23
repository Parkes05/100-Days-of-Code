import sys
sys.path.append('../Data')

from turtle import Screen, Turtle
from snake_class_20_21 import Snake
from food_class_20_21 import Food
from scoreboard_20_21 import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 7.5:
        food.new_food()
        snake.add_snake()
        score_board.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False  
        score_board.game_over()
        snake.reset_snake()
    
    for segments in snake.turtles[1:]:
        if snake.head.distance(segments) < 5:
            # game_is_on = False 
            score_board.game_over()
            snake.reset_snake()

screen.exitonclick()