from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600) #defining screen dimensions
screen.bgcolor("black") # black background
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update() # only update screen once all segments have moved forward
    time.sleep(0.1)

    snake.move()





screen.exitonclick()