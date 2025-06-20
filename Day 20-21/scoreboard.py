from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.score = 0
        file = open("Day 20-21/data.txt", mode = "r")
        self.high_score = int(file.read())
        file.close()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        #self.write(f"Score: {self.score}", align = "center", font = ('Arial', 24, 'normal'))
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)
        
    def addScore(self): # increase score
        self.score += 1
        self.update_scoreboard()
        
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("Day 20-21/data.txt", mode = "w")
            file.write(str(self.score))
            file.close()
            
        self.score = 0
        self.update_scoreboard()
        