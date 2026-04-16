from turtle import Turtle, Screen
import random

move = Turtle()

colours = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta']

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        move.forward(100)
        move.right(angle)

for shape_side_n in range(3, 11):
    move.color(random.choice(colours)) #each shape is a random colour
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()




