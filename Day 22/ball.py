from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.goto(x=-200, y=0)
        
    def ball_physics(self):

        
        self.forward(10)

        if self.ycor() > 290:
            self.right(90)