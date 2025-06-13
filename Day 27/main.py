import tkinter

window = tkinter.Tk()

window.title("My forst GUI program")
window.minsize(width=500, height= 300)

# Create a label (component)
my_label = tkinter.Label(text = "I am a label", font = ("Arial", 24, "bold"))
my_label.pack(expand = True) # untuk pack label into the screen











window.mainloop() # Always at the end of the code