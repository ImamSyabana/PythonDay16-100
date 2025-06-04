from turtle import Turtle, Screen
from paddle_LR import Paddle_LR
from ball import Ball
import time

screen = Screen()
screen.setup(width = 800, height= 600)
screen.bgcolor("black")
screen.title("pong game")
screen.tracer(0)

# membuat paddle kanan
right_paddle = Paddle_LR(350, 0)
left_paddle = Paddle_LR(-350, 0)

#object ball 
ball = Ball()

# menerima input penggerak paddle

screen.listen()
screen.onkey(right_paddle.down, "Down")
screen.onkey(right_paddle.up, "Up")

screen.onkey(left_paddle.down, "s")
screen.onkey(left_paddle.up, "w")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    # menggerakan bola pertama ke kanan atas
    ball.move()
    
    # detect collision with wall
    if ball.ycor() >290 or ball.ycor() < -290:
        ball.bounce()
    
    
        
screen.exitonclick()

