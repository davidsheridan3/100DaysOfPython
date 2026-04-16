from turtle import Turtle, Screen
import random

move = Turtle()

colours = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta']
directions = [0, 90, 180, 270]
move.pensize(15) #adjusting line width
move.speed("fastest") #adjusting speed of animation


for _ in range(200):
    move.color(random.choice(colours))
    move.forward(30)
    move.setheading(random.choice(directions))