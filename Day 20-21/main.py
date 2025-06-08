from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food 
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake= Snake() # Creating the snake
food = Food() # Creating the food
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move() # Moving the snake
    
    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.clear()
        score.addScore()
        
    # Detect collision with wall.
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        score.reset()
        snake.reset()
        

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        
        # if segment == snake.head:
        #     pass
        
        # elif snake.head.distance(segment) < 10:
        #     game_is_on = False
        #     score.game_over()
            
        if snake.head.distance(segment) < 10:
            
            score.game_over()
            
   
    
screen.exitonclick()


