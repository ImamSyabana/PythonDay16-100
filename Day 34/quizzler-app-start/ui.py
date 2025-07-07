import tkinter
from tkinter import PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady= 20)
        self.window.configure(background=THEME_COLOR)
        
        self.score_text = tkinter.Label(text = "Score: 0", bg=THEME_COLOR, fg='white', font = ('Arial', 12, 'bold'))
        self.score_text.grid(column=1, row=0,  padx=20, pady=20)
        
        self.canvas = tkinter.Canvas(width = 300, height=250)
        
        self.question_text = self.canvas.create_text(
            150, 
            125,
            width=280,
            
            text = "Click to begin!", 
            font = ('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)  
              
        correctImage = PhotoImage(file="Day 34/quizzler-app-start/images/true.png")
        self.correctButton = tkinter.Button(image = correctImage, highlightthickness=0, command=self.true_pressed)
        self.correctButton.grid(column=0, row=2, padx=20, pady=20)
        
        wrongImage = PhotoImage(file="Day 34/quizzler-app-start/images/false.png")
        self.wrongButton = tkinter.Button(image = wrongImage, highlightthickness=0, command=self.false_pressed)
        self.wrongButton.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg = "White")
        if self.quiz.still_has_questions():
            self.score_text.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You have reached the end of the quiz.")
            self.correctButton.config(state = "disabled")
            self.wrongButton.config(state = "disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def bg_toRed(self):
        self.canvas.configure(bg = "Red")
        
    def bg_toGreen(self):
        self.canvas.configure(bg = "Green")
        
    def bg_toWhite(self):
        self.canvas.configure(bg = "White")
        
    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.configure(bg= "Green")
            self.window.after(1000, self.get_next_question)
         
        elif is_right == False:
            self.canvas.configure(bg= "Red")
            self.window.after(1000, self.get_next_question)
            