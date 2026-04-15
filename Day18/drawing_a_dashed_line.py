from turtle import Turtle, Screen

draw_line = Turtle()

for i in range(40):
    draw_line.forward(20)
    draw_line.up()
    draw_line.forward(20)
    draw_line.down()

screen = Screen()
screen.exitonclick()
