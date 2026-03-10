from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle") #changing the shape of the turtle
timmy.color("red") #changing the color of the turtle
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable # installed prettytable package to make a table

table = PrettyTable()
table.add_column("Name", ["Angela", "David", "Joseph"])
table.add_column("Age", [25, 22, 23])
table.align = "l"

print(table)