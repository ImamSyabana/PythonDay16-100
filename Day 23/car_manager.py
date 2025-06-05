COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import time
import random
from turtle import Turtle 
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        
        self.all_cars = []
        self.hideturtle()
        
        
    def create_car(self):
        random_chance = random.randint(1,6)
        
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.goto(x = 320, y = random.randint(-250,250))
            
            new_car.movement_speed = STARTING_MOVE_DISTANCE
            new_car.increase_speed = MOVE_INCREMENT
            
            new_car.setheading(180)
            self.all_cars.append(new_car)
        
    def move_sideways(self, tambah_kecepatan):
        for x in range(len(self.all_cars)):
            self.all_cars[x].forward(self.all_cars[x].movement_speed + tambah_kecepatan)

        
        
            
    

       
