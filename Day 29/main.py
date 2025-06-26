import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    #password_list = []

    password_list = [random.choice(letters) for pw in range(nr_letters)]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_list = password_list + [random.choice(symbols) for char in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_list = password_list + [random.choice(numbers) for char in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char
    
    Password_input.insert(0, password)
    
    # copy ke clipboard
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file():
    
    website = website_input.get()
    password = Password_input.get()
    email = userName_input.get()
    
    new_data = {
        website: {
            "email" : email,
            "password" : password
        }
    }
    if len(website_input.get()) == 0 or len(Password_input.get()) == 0:
        messagebox.showwarning(
            title="Oops",
            message=f"Please don't leave any fields empty!"
        )
        is_ok = None
    
    
    else:
        #is_ok = True
        is_ok = messagebox.askokcancel(
        title = website_input.get(), 
        message=f"These are the details entered: \nEmail: {userName_input.get()} \nPassword: {Password_input.get()} \nIs it ok to save?"
    )

    if is_ok == None:
        pass
    else:
        try:
            with open("Day 29/pass_saveFile.json", "r") as data_file:
                # # ini kalo mau write ke file txt yang biasa
                # data_file.write(f"{website_input.get()} | {userName_input.get()} | {Password_input.get()}\n")
                
                
                # # kalo mau write ke file json agak laen, make dump
                # json.dump(new_data, data_file, indent=4)
                
                # untuk membaca json file makke json load
                # nanti beruba dari format json ke python dictionary
                data = json.load(data_file) # read old data

        except FileNotFoundError:    
            with open("Day 29/pass_saveFile.json", "w") as data_file: 
                # saving updated data
                json.dump(new_data, data_file, indent=4)
                        
        else:
    
            # untuk menambahkan data ke json file gunakan json update
            data.update(new_data) # updating old data with new data      
            
            with open("Day 29/pass_saveFile.json", "w") as data_file: 
                # saving updated data
                json.dump(data, data_file, indent=4)
            

        finally:
            website_input.delete(0, "end")
            Password_input.delete(0, "end")
        
# ------------------------ Data Search Modul -------------------------- #
def find_password():
    try:   
        with open("Day 29/pass_saveFile.json", "r") as data_file:
            data = json.load(data_file) # read old data
            
    except FileNotFoundError:
        messagebox.showwarning(
        title="Data doesn't exist",
        message=f"No Data File Found.")
        
    else:
            try:
                mail_pass_dict = data[website_input.get()] # dicari berdasarkan nama sitenya terus hasilnya email sama password terdaftar untuk site tersebut
                
            except KeyError:
                messagebox.showwarning(
                title="Key doesn't exist",
                message=f"No details for the website exists."
            )
                
            else:
                messagebox.showinfo(
                title = website_input.get(), 
                message=f"Email: {data[website_input.get()]["email"] } \nPassword: {data[website_input.get()]["password"] }"
                )
            
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
website_input = tkinter.Entry(width=23)
website_input.grid(column=1, row = 1)
website_input.focus()

userName_input = tkinter.Entry(width=42)
userName_input.grid(column=1, row = 2, columnspan= 2 )
userName_input.insert(0, "zelkova46@gmail.com")

Password_input = tkinter.Entry(width=23)
Password_input.grid(column=1, row = 3)

# button
gen_password = tkinter.Button(text = "Generate password", command=generate_password)
gen_password.grid(column=2, row = 3)

search_btn = tkinter.Button(text = "Search", width=15, command= find_password)
search_btn.grid(column=2, row = 1)
    
add_btn = tkinter.Button(text = "Add", width=35, command=save_file)
add_btn.grid(column=1, row = 4,columnspan=2)


window.mainloop()