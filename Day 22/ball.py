from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.goto(x=-200, y=0)
        self.x_move = 10
        self.y_move = 10
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x = new_x, y = new_y)
        
    def bounce(self):
        self.y_move = self.y_move * -1