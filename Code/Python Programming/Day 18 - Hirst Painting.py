import turtle as t
import random



# Exercise 1
turtle_timmy = t.Turtle()
turtle_timmy.shape('turtle')

colours = ['black' , 'red' , 'green' , 'blue' , 'cyan' , 'yellow' , 'magenta']

def number_of_sides(sides, turtle_passed):
    angle = 360 / sides
    for _ in range(sides):
        turtle_passed.forward(100)
        turtle_passed.right(angle)

for sides in range(3, 6):
    turtle_timmy.color(random.choice(colours))
    number_of_sides(sides, turtle_timmy)



# Exercise 2
turtle_timmy.clear()
turtle_timmy.hideturtle()
turtle_tom = t.Turtle()
turtle_tom.shape('arrow')
turtle_tom.width(10)
turtle_tom.speed(0)
t.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

direction = [0, 90, 180, 270]
for _ in range(200):
    turtle_tom.color(random_colour())
    degree = random.choice(direction)
    turtle_tom.setheading(degree)
    turtle_tom.forward(30)



# Exercise 3
turtle_tom.clear()
turtle_tom.hideturtle()
turtle_sam = t.Turtle()
turtle_sam.speed(0)
turtle_sam.shape('square')

def circle_heading(tilt):
    for _ in range(int(360 / tilt)):
        turtle_sam.color(random_colour())
        turtle_sam.circle(100)
        turtle_sam.setheading(turtle_sam.heading() + tilt)

circle_heading(5)



# Project - Hirst Painting
import colorgram

def colour_extractor(image, num):
    new_colour = colorgram.extract(image, num)
    colours = []
    for i in range(num):
        rgb = new_colour[i].rgb
        red = rgb.r
        green = rgb.g
        blue = rgb.b
        colours.append((red, green, blue))
    return colours

# print(colour_extractor('image_18.jpg', 30))
colour_list = [
    (24, 24, 61), (183, 73, 38), (144, 17, 31), (39, 29, 21), 
    (214, 145, 85), (124, 159, 216), (204, 73, 115), 
    (68, 26, 35), (55, 92, 138), (37, 45, 126), (23, 33, 23), 
    (161, 21, 14), (142, 57, 80), (71, 78, 32), (67, 113, 74), 
    (100, 98, 192), (141, 178, 161), (207, 77, 62), (144, 213, 191),
    (98, 168, 76), (192, 141, 156), (49, 85, 26), (156, 210, 221), 
    (225, 172, 184), (175, 185, 221),
    ] 

turtle_zack = t.Turtle()
turtle_zack.hideturtle()
turtle_zack.penup()
turtle_zack.speed(10)

def painting(j):
    x = -200
    y = -200
    new_y = y + 50 * j
    for i in range(10):
        new_x = x + 50 * i
        turtle_zack.setposition(new_x, new_y)
        turtle_zack.dot(20, random.choice(colour_list))
    
for position in range(10):
    painting(position)   
    


screen = t.Screen()
screen.exitonclick()