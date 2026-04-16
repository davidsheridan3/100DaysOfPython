import turtle
import random

move = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b) #tuple

directions = [0, 90, 180, 270]
move.pensize(15) #adjusting line width
move.speed("fastest") #adjusting speed of animation


for _ in range(200):
    move.color(random_color()) #introducing completely random, instead of previous list
    move.forward(30)
    move.setheading(random.choice(directions))