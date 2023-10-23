from turtle import Turtle, Screen

# # Exercise 1
timmy = Turtle()
screen = Screen()
timmy.speed(0)
DISTANCE = 10
ANGLE = 10

def forwards():
    timmy.forward(DISTANCE)

def backward():
    timmy.backward(DISTANCE)

def counterclockwise():
    timmy.setheading(timmy.heading() + ANGLE)

def clockwise():
    timmy.setheading(timmy.heading() - ANGLE)

def clear():
    timmy.reset()

screen.listen()
screen.onkey(key = 'w', fun = forwards)
screen.onkey(key = 's', fun = backward)
screen.onkey(key = 'a', fun = counterclockwise)
screen.onkey(key = 'd', fun = clockwise)
screen.onkey(key = 'c', fun = clear)
screen.exitonclick()



# Project
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput('Colour Guessing Game', 'Choose a colour. "red", "yellow", "blue", "green", "purple" or "indigo"')

colour_list = ['red', 'yellow', 'blue', 'green', 'purple', 'indigo']
all_turtles = []
y = -70

for position in range(6):
    timmy = Turtle(shape='turtle')
    timmy.penup()
    timmy.color(colour_list[position])
    timmy.setposition(x=-230, y=y)
    y += 30
    all_turtles.append(timmy)

is_game_on = False

if user_input:
    is_game_on = True

while is_game_on:

    for turtle in all_turtles:
        if is_game_on:
            random_num = random.randint(0, 10)
            turtle.forward(random_num)

        if turtle.position()[0] >= 230:
            is_game_on = False
            winner = turtle

if user_input == winner.pencolor():
    print(f'Congratulations, you win!. Winning colour is {winner.pencolor()}')
else:
    print(f'Sorry, you lose. Winning colour is {winner.pencolor()}')



screen.exitonclick()