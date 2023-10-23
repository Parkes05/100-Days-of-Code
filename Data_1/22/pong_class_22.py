from turtle import Turtle

MOVE = 20
FONT = ('Courier', 80, 'normal')
    
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.setposition(position)
        self.shapesize(stretch_wid=5, stretch_len=1)
    
    def pad_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + MOVE
            self.setposition(self.xcor(), new_y)

    def pad_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - MOVE
            self.setposition(self.xcor(), new_y)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.setposition(0, 0)
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def ball_move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.setposition(new_x, new_y)

    def ball_bounce_y(self):
        self.y *= -1
    
    def ball_bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.9

    def score(self):
        self.setposition(0, 0)
        self.move_speed = 0.1
        self.ball_bounce_x()
    
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.setposition(-100, 200)
        self.write(arg=self.l_score, align="center", font=FONT)
        self.setposition(100, 200)
        self.write(arg=self.r_score, align="center", font=FONT)
    
    def point_r(self):
        self.r_score += 1
        self.update_score()

    def point_l(self):
        self.l_score += 1
        self.update_score()

