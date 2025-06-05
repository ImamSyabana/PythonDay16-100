FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(x = -200, y = 250)
        self.write(arg = "Level: {score}".format(score = self.score), align = "center", font = FONT)
        
    def addScore(self):
        self.score = self.score + 1
        self.update_scoreboard()
        
    def game_terminate_message(self):
        self.goto(x = 0, y = 0)
        self.write(arg = "GAME OVER", align="center", font = FONT)
