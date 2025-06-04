from turtle import Turtle, Screen
from paddle_R import Paddle_R

screen = Screen()
screen.setup(width = 800, height= 600)
screen.bgcolor("black")
screen.title("pong game")

# membuat paddle kanan
right_paddle = Paddle_R()

# menerima input penggerak paddle
screen.listen()
screen.onkey(right_paddle.down, "Down")
screen.onkey(right_paddle.up, "Up")


screen.exitonclick()

