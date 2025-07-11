import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps  = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer(): # merubah semua GUI menjadi keadaan semula 
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text = "Timer")
    checkMark.config(text = "")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps = reps + 1
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 2 != 0:
        count_down(work_sec)
        title_label.config(text="Work!", fg = GREEN)
        
    elif reps % 2 == 0 and reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long break!", fg = RED)

    elif reps % 2 == 0 :
        count_down(short_break_sec)
        title_label.config(text="Short break!", fg = PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import math
def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60
    
    if sec < 10: # Dynamic typing
        sec = f"0{sec}" # merubah tipe data
        
    canvas.itemconfig(timer_text, text = f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkMark.config(text = int(reps / 2) * "✓")
            
            
    
    
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)


canvas  = tkinter.Canvas(width = 200, height  = 224, bg = YELLOW, highlightthickness = 0)

tomato_img = tkinter.PhotoImage(file = "Day 28/tomato.png")
canvas.create_image(100, 112, image = tomato_img)

timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row= 2)




title_label = tkinter.Label(text = "Timer", font = (FONT_NAME, 40, "bold"), bg = YELLOW, fg= GREEN)
title_label.grid(column=1, row= 0)

startButton = tkinter.Button(text = "start", command= start_timer)
startButton.grid(column=0, row=3)

resetButton = tkinter.Button(text = "reset", command= reset_timer)
resetButton.grid(column=2, row = 3)

checkMark = tkinter.Label(text = "", font = (FONT_NAME, 14, "bold"), bg = YELLOW, fg= GREEN)
checkMark.grid(column = 1, row = 4)
window.mainloop()