from turtle import Turtle

class Paddle_LR(Turtle):
    def __init__(self, posX, posY):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)  # Adjust size as needed
        self.goto(x=posX, y=posY)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)
