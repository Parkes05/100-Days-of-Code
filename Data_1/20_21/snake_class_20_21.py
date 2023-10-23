from turtle import Turtle

MOVE_DISTANCE = 10
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def my_turtle(self, position):
        new_turtle = Turtle(shape='square')
        new_turtle.color('white')
        new_turtle.shapesize(0.5)
        new_turtle.penup()
        new_turtle.setposition(position)
        self.turtles.append(new_turtle)

    def create_snake(self):
        x_position = 0
        for _ in range(3):
            self.my_turtle((x_position, 0))
            x_position -= 10

    def add_snake(self):
        new_position = self.turtles[-1].position()
        self.my_turtle(new_position)
    
    def reset_snake(self):
        for seg in self.turtles:
            seg.setposition(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def move(self):
        for index in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[index - 1].xcor()
            new_y = self.turtles[index - 1].ycor()
            self.turtles[index].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

