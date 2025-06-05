STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color = "black"
        self.shape("turtle")
        self.penup()
        
        self.start_pos = STARTING_POSITION
        self.goto(STARTING_POSITION)
        self.move_distance = MOVE_DISTANCE
        self.setheading(90)
        
    def move_forward(self):
        self.forward(distance=MOVE_DISTANCE)
