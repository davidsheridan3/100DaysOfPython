# import turtle
# tim = turtle.Turtle() #tedious specifying both the module and class name
#
#
# from turtle import Turtle

# Creating multiple turtles is so much easier when we have the specific class defined in import
tim = Turtle()
tom = Turtle()
david = Turtle()

# from turtle import * # allows us to import all classes in module
import turtle as t # assigning the module a custom name
tim = t.Turtle()

