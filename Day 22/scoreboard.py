from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        
        # update score
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(x = 100, y =200)
        self.write(self.r_score, align = "center", font = ("Courier", 60, "normal"))
        self.goto(x = -100, y =200)
        self.write(self.l_score, align = "center", font = ("Courier", 60, "normal"))
        

        
        
    def addScore_l_paddle(self):  
        self.l_score = self.l_score + 1 
        self.update_scoreboard()
        
    def addScore_r_paddle(self):
        self.r_score = self.r_score + 1 
        self.update_scoreboard()
        