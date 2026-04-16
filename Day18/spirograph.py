import turtle
import random

move = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color =  (r,g,b)
    return color

move.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        move.color(random_color())
        move.circle(100)
        move.setheading(move.heading() + size_of_gap)

draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()