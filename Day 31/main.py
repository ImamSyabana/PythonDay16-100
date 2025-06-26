BACKGROUND_COLOR = "#B1DDC6"

import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
from tkinter import PhotoImage
import pandas as pd
import random

FONT_NAME = "Courier"

# --------------------------- Data Read -----------------------------------------------
# read the data

try:
    words_data = pd.read_csv("Day 31/data/words_to_learn.csv")
    
except FileNotFoundError:
    words_data = pd.read_csv("Day 31/data/french_words.csv")
    
finally:
    words_data = words_data.to_dict(orient="records")

# for the initialization
rand_words= random.randint(0, len(words_data) -1 )

# deleting a memorized word
def known_words():
    global rand_words
    words_data.pop(rand_words)
    
    if words_data:
        words_to_learn_en = [words["English"] for words in words_data]
        words_to_learn_fr = [words["French"] for words in words_data]
        
        dict_words = {
            "French" : words_to_learn_fr,
            "English" : words_to_learn_en
            }    

        df_dict = pd.DataFrame(dict_words)
        
        # saving the dataframe
        df_dict.to_csv('Day 31/data/words_to_learn.csv', header=False, index=False)
        
        rand_words = random.randint(0, len(words_data) - 1)
    
    else:
        # If no words left, handle accordingly (e.g., show a message)
        messagebox.showinfo("Congratulations!", "You've learned all the words!")
        rand_words = None
# for the randomizer button
def pick_random_words():
    global rand_words
    rand_words= random.randint(0, len(words_data)-1)

    canvas.itemconfig(words_canvas, text=words_data[rand_words]["French"])
    
    # excecute fungsi untuk generate sisa kata untuk dihapal
    known_words()
    
    # generate transisi dari en ke france
    en_to_fr()

# ------------------------------ UI -------------------------------------------------
window = tkinter.Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50)
window.config(bg=BACKGROUND_COLOR)


    
# canvas object
canvas = tkinter.Canvas(width=800, height=526, bg = BACKGROUND_COLOR, highlightthickness = 0)

card_back_img = tkinter.PhotoImage(file = "Day 31/images/card_back.png")
card_front_img = tkinter.PhotoImage(file = "Day 31/images/card_front.png")
card_switch = canvas.create_image(400, 263, image = card_front_img)
canvas.grid(column=0, row=0, columnspan= 2)


def en_to_fr():
    canvas.itemconfig(card_switch, image = card_front_img)
    canvas.itemconfig(lang_canvas, fill = "black", text= "French")
    canvas.itemconfig(words_canvas, fill = "black", text=words_data[rand_words]["French"])
    window.after(3000, fr_to_en)
    
def fr_to_en():
    canvas.itemconfig(card_switch, image = card_back_img)
    canvas.itemconfig(lang_canvas, fill = "white", text = "English")
    canvas.itemconfig(words_canvas, fill = "white", text=words_data[rand_words]["English"])
    
    
    
window.after(3000, fr_to_en)
# card_back_img = tkinter.PhotoImage(file = "Day 31/images/card_back.png")
# canvas.create_image(400, 263, image = card_back_img)
# canvas.grid(column=0, row=0, columnspan= 2)



# membuat button dengan gambar
right_image = PhotoImage(file="Day 31/images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=pick_random_words)
right_button.grid(column=1, row = 1)

wrong_image = PhotoImage(file="Day 31/images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=pick_random_words)
wrong_button.grid(column=0,row = 1)


    

# label dalam card (French side)
lang_canvas = canvas.create_text(400, 150, text="French", font = ("Ariel", 40, "italic"))
canvas.grid(column=0, row=0)

words_canvas = canvas.create_text(400, 263, text=words_data[rand_words]["French"], font = ("Ariel", 60, "bold"))
canvas.grid(column=0, row=0)




print(words_data[rand_words]["French"])
print(words_data[rand_words]["English"])

print((words_data[rand_words].keys()))

print(words_data[rand_words])

print(words_data)



window.mainloop()