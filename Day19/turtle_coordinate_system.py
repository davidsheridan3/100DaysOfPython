from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_postions = [-70, -40, -10, 20, 50, 80]




for each_color in colors:
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(each_color)
    tim.goto(-230, y_postions[colors.index(each_color)])







screen.exitonclick()