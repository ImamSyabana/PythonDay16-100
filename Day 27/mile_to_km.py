import tkinter

# init window
window = tkinter.Tk()

window.title("Mile to Km Converter")
window.minsize(width=240, height= 140)
window.config(padx =20, pady = 20)

# menambahkan padding
#window.config()

# Create a label (component)
my_label = tkinter.Label(text = "is equal to")
my_label.grid(column = 0, row = 1) # untuk pack label into the screen
my_label.config(padx =10, pady = 10)

# Button

def miles_to_km():
    #my_label["text"] = "Button Got Clicked"
    km_input.delete(0, tkinter.END)
    km_input.insert(tkinter.END, string = f"{float(miles_input.get()) * 1.60934}")
    


# Entry untuk masukkin miles
miles_input = tkinter.Entry(width=10)
print(miles_input.get())
miles_input.grid(column = 1, row = 0)


# Entry untuk masukkin km
km_input = tkinter.Entry(width=10)
print(km_input.get())
km_input.grid(column = 1, row = 1)

# Create a label (component)
miles_label = tkinter.Label(text = "Miles")
miles_label.grid(column = 2, row = 0) # untuk pack label into the screen
miles_label.config(padx =0, pady = 0)

km_label = tkinter.Label(text = "Km")
km_label.grid(column = 2, row = 1) # untuk pack label into the screen

calculate_btn = tkinter.Button(text="Calculate", command = miles_to_km)
calculate_btn.grid(column=1, row=2)

window.mainloop() # Always at the end of the code..

# reboisasi
# reboisasi