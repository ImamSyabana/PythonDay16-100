import tkinter
from tkinter import messagebox

FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 20)

canvas = tkinter.Canvas(width=200, height=200)

logo = tkinter.PhotoImage(file = "Day 29/logo.png")
canvas.create_image(100,100, image = logo)
canvas.grid(column=0, row = 0, columnspan=3)

# label
websiteName_label = tkinter.Label(text = "Website:", font = (FONT_NAME, 12, "bold"))
websiteName_label.grid(column=0, row=1, padx=10)

userName_label = tkinter.Label(text = "Email/Username:", font = (FONT_NAME, 12, "bold"))
userName_label.grid(column=0, row=2, padx=10)

Password_label = tkinter.Label(text = "Password:", font = (FONT_NAME, 12, "bold"))
Password_label.grid(column=0, row=3, padx=10)

# input col
website_input = tkinter.Entry(width=42)
website_input.grid(column=1, row = 1, columnspan= 2)
website_input.focus()

userName_input = tkinter.Entry(width=42)
userName_input.grid(column=1, row = 2, columnspan= 2 )
userName_input.insert(0, "zelkova46@gmail.com")

Password_input = tkinter.Entry(width=23)
Password_input.grid(column=1, row = 3)

# button
gen_password = tkinter.Button(text = "generate password")
gen_password.grid(column=2, row = 3)

def save_file():
    
    if len(website_input.get()) == 0 or len(Password_input.get()) == 0:
        messagebox.showwarning(
            title="Oops",
            message=f"Please don't leave any fields empty!"
        )
        is_ok = None
        
    else:
        is_ok = messagebox.askokcancel(
        title = website_input.get(), 
        message=f"These are the details entered: \nEmail: {userName_input.get()} \nPassword: {Password_input.get()} \nIs it ok to save?"
    
        
    )

    if is_ok == None:
        pass
    elif is_ok:
        with open("Day 29/pass_saveFile.txt", "a") as f:
            f.write(f"{website_input.get()} | {userName_input.get()} | {Password_input.get()}\n")
            
        website_input.delete(0, "end")
        Password_input.delete(0, "end")
    
    
add_btn = tkinter.Button(text = "Add", width=35, command=save_file)
add_btn.grid(column=1, row = 4,columnspan=2)


window.mainloop()