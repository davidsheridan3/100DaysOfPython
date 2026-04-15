from turtle import Turtle, Screen

draw_square = Turtle()
# draw_square.forward(100)
# draw_square.left(90)
# draw_square.forward(100)
# draw_square.left(90)
# draw_square.forward(100)
# draw_square.left(90)
# draw_square.forward(100)


# Because we are programmers and don't like seeing repeated code, we use for loop
for i in range(4):
    draw_square.forward(100)
    draw_square.left(90)

screen = Screen()
screen.exitonclick()
