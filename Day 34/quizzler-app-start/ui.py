import tkinter
from tkinter import PhotoImage

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady= 20)
        self.window.configure(background=THEME_COLOR)
        
        self.score_text = tkinter.Label(text = "Score: 0", bg=THEME_COLOR, fg='white', font = ('Arial', 12, 'bold'))
        self.score_text.grid(column=1, row=0,  padx=20, pady=20)
        
        self.canvas = tkinter.Canvas(width = 300, height=250)
        
        self.question = self.canvas.create_text(150, 125, text = "Click to begin!", font = ('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)  
              
        correctImage = PhotoImage(file="Day 34/quizzler-app-start/images/true.png")
        self.correctButton = tkinter.Button(image = correctImage, highlightthickness=0)
        self.correctButton.grid(column=0, row=2, padx=20, pady=20)
        
        wrongImage = PhotoImage(file="Day 34/quizzler-app-start/images/false.png")
        self.wrongButton = tkinter.Button(image = wrongImage, highlightthickness=0)
        self.wrongButton.grid(column=1, row=2, padx=20, pady=20)

        self.window.mainloop()