from turtle import Turtle, Screen
from paddle_LR import Paddle_LR
from ball import Ball
import time
from scoreboard import Scoreboard

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

# object score
scoreboard = Scoreboard()

# menerima input penggerak paddle

screen.listen()
screen.onkey(right_paddle.down, "Down")
screen.onkey(right_paddle.up, "Up")

screen.onkey(left_paddle.down, "s")
screen.onkey(left_paddle.up, "w")

game_is_on = True



while game_is_on:
    screen.update()
    # the lower the faster
    time.sleep(ball.move_speed)
    
    # menggerakan bola pertama ke kanan atas
    ball.move()
    
    # detect collision with wall
    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()
    
        
    # detect collision with r and L paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed = ball.move_speed * 0.9
        #print(ball.move_speed)
        
    #detect if the ball pass the right paddle
    if ball.xcor() > 380:
        scoreboard.addScore_l_paddle()
        ball.restart_condition()

    # detect of the vall pass the left paddle
    if ball.xcor() < -380:
        scoreboard.addScore_r_paddle()
        ball.restart_condition()
        
        
        

        
screen.exitonclick()

