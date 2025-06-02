from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)   
        turtle.forward(random_distance)
    
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won! The {winning_color} turtle is the winner!".format(winning_color=winning_color))
            else:
                print("You've lost! The {winning_color} turtle is the winner!".format(winning_color=winning_color))
                
            is_race_on = False
screen.exitonclick()