from turtle import Turtle, Screen
import time
import snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    
    
    
screen.exitonclick()


