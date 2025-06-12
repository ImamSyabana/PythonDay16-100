import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day 25_US_game/blank_states_img.gif"
screen.addshape(image)
screen.screensize(600, 600)
turtle.shape(image)
turtle.penup()

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# import dataset
dataset = pd.read_csv("Day 25_US_game/50_states.csv")

# def get_mouse_click_coor(x, y):
#     print(x, y)
    
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


#print(answer_state)

# list daftar states
state_list = dataset["state"]
state_list = state_list.to_list()
#print(state_list[:])
#print(type(state_list))

print((dataset[dataset["state"] == "Ohio"]["state"].values[0]))
print((dataset[dataset["state"] == "Ohio"]["x"]).values[0])
print((dataset[dataset["state"] == "Ohio"]["y"]).values[0])


# Bagian untuk menebak semua state
num_guessed_state= 0
correct_guessed_state = []
jumlah_state = len(state_list)
while len(state_list) > 0:  
    # Read from the csv and gather the coordinate information
    answer_state = screen.textinput(title = "{ditebak} / {total} States Correct".format(ditebak = num_guessed_state, total = jumlah_state), prompt = "What is another state's name?")

    # Convert guesses to tittle case
    answer_state = answer_state.title()
    
    if answer_state == "Exit":
        break
    #print(state)
    for state in state_list:
        if answer_state == (dataset[dataset["state"] == state]["state"].values[0]):
            writer.goto(x = (dataset[dataset["state"] == state]["x"].values[0]), y = (dataset[dataset["state"] == state]["y"].values[0]))
            writer.write(arg = (dataset[dataset["state"] == state]["state"].values[0]), align = "center")
            state_list.pop(state_list.index(state))
            correct_guessed_state.append(state)
            num_guessed_state = num_guessed_state + 1
        else:
            continue
            
        print("Current Score: {ditebak}/{total}".format(ditebak = num_guessed_state, total = jumlah_state))
        print(correct_guessed_state)

# state_to_learn.csv (generate file yang berisi nama nama state yang belum disebut)

state_list = dataset["state"]
state_list = state_list.to_list()

missed_state = []
for state in state_list:
    if state not in correct_guessed_state:
        missed_state.append(state)

print(f"Missed states: {missed_state}")
# Converting to csv
missed_state_dict = {"state to learn": missed_state}

df = pd.DataFrame(missed_state_dict)

# saving to a csv file.
df.to_csv("Day 25_US_game/state_to_learn.csv")
