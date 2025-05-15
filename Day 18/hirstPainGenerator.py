import turtle
from turtle import Turtle, Screen
import random

colorList = [(192, 2, 109), (225, 105, 2), (17, 145, 63), (183, 164, 1), (52, 21, 176), (13, 178, 75), (41, 28, 18), (55, 16, 43), (21, 30, 52), (20, 34, 25), (180, 21, 209), (191, 3, 254), (178, 10, 4), (29, 128, 142), (21, 95, 41), (198, 9, 247), (96, 81, 6), (235, 117, 29), (235, 61, 26), (15, 86, 96), (20, 158, 166), (122, 6, 252), (97, 164, 124), (117, 112, 152), (121, 134, 156)]

ninjaTurtle = Turtle()
ninjaTurtle.shape("arrow")

turtle.colormode(255)
ninjaTurtle.penup()


ninjaTurtle.goto(-250, -250)




for baris in range(10):
    for kolom in range(10):
        ninjaTurtle.dot(20, random.choice(colorList))
        ninjaTurtle.forward(50)
    
    
    ninjaTurtle.sety(-250 + ((baris + 1) * 50))
    ninjaTurtle.setx(-250)

print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")










screen = Screen()
screen.exitonclick()