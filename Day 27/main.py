import tkinter

# init window
window = tkinter.Tk()

window.title("My forst GUI program")
window.minsize(width=500, height= 300)

# menambahkan padding
window.config(padx = 20, pady = 20)

# Create a label (component)
my_label = tkinter.Label(text = "I am a label", font = ("Arial", 24, "bold"))
my_label.pack() # untuk pack label into the screen

# buat ngeganti label yang udah dibikin di atas
my_label["text"] = "New Text" # bisa pake yang ini 
my_label.config(text = "New Text") # atau pake yang ini
my_label.grid(column=0, row = 0)
my_label.config(padx = 20, pady = 20)

# Button

def button_clicked():
    #my_label["text"] = "Button Got Clicked"
    my_label.config(text = input.get())
    
button = tkinter.Button(text = "Click Me", command = button_clicked)
button.grid(column = 1, row = 1)

# Entry (input function)
input = tkinter.Entry(width=30)
print(input.get())
input.grid(column = 3, row = 2)

new_button = tkinter.Button(text="New Button", command = button_clicked)
new_button.grid(column=2, row=0)

window.mainloop() # Always at the end of the code