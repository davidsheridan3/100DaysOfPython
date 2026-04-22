from turtle import Screen, Turtle

screen = Screen()
screen.setup(600, 600) #defining screen dimensions
screen.bgcolor("black") # black background
screen.title("Snake Game")

# segment_1 = Turtle(shape="square")
# segment_1.color("white") # adapting colour of square to background
#
# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(-20, 0)
#
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto(20, 0)

# I found this way to be tedious and there was too much repetition, so I used a for loop instead....

starting_positions = [(0, 0),(20, 0),(-20, 0)]

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)





screen.exitonclick()