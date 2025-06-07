import time
from turtle import Screen
from player import Player
from car_manager import CarManager, MOVE_INCREMENT
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()

# object score
scoreboard = Scoreboard()

screen.listen()

screen.onkey(turtle.move_forward, "w")

tambah_kecepatan = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if turtle.ycor() > 250:
        turtle.goto(turtle.start_pos)
        tambah_kecepatan = tambah_kecepatan + MOVE_INCREMENT
        scoreboard.addScore()
    
    car_manager.create_car()
    car_manager.move_sideways(tambah_kecepatan)
    
    
    for collision in range(len(car_manager.all_cars)):
        if abs(turtle.xcor() - car_manager.all_cars[collision].xcor()) < 25 and abs(turtle.ycor() - car_manager.all_cars[collision].ycor()) < 20:
            scoreboard.game_terminate_message()
            game_is_on = False
        
    

   
screen.exitonclick()
# dsadsad