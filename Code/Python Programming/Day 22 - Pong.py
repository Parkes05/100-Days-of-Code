import sys
sys.path.append('../Data')
from pong_class_22 import Paddle, Ball, Score
from turtle import Screen
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(fun=r_paddle.pad_up, key='Up')
screen.onkeypress(fun=r_paddle.pad_down, key='Down')
screen.onkeypress(fun=l_paddle.pad_up, key='w')
screen.onkeypress(fun=l_paddle.pad_down, key='s')

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.ball_bounce_x()
    
    if ball.xcor() > 380:
        ball.score()
        score.point_l()

    if ball.xcor() < -380:
        ball.score()
        score.point_r()

screen.exitonclick()
