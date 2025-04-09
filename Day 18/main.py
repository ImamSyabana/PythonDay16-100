from turtle import Turtle, Screen
import random

ninjaTurtle = Turtle()
ninjaTurtle.shape("arrow")
ninjaTurtle.color("darkSlateGray")

# Pause number 1 - create a square
for x in range(4):
    ninjaTurtle.forward(100)
    ninjaTurtle.right(90)

# pause 2 - draw a dash line
ninjaTurtle.reset()

for x in range(20):
    ninjaTurtle.forward(5)
    ninjaTurtle.penup()
    ninjaTurtle.forward(5)
    ninjaTurtle.pendown()


# pause 3 - macam2 bangun datar
ninjaTurtle.reset()

ninjaTurtle.speed(9)

sidesNumber = 3
decagon = 10

colorList = ["DarkRed", "Darkorchid4", "lightSalmon", "cadetBlue", 
             "HotPink", "greenYellow", "magenta4", "navy"]

while sidesNumber < decagon:
    for x in range(sidesNumber):
        ninjaTurtle.forward(100)
        ninjaTurtle.right(360/sidesNumber)
        
    ninjaTurtle.color(random.choice(colorList))
    sidesNumber = sidesNumber + 1
    
    
# pause 4 - random walk
ninjaTurtle.reset()

ninjaTurtle.pensize(10)


def goStraight():
    ninjaTurtle.forward(20)
    
def goLeft():
    ninjaTurtle.left(90)
    ninjaTurtle.forward(20)
    
def goRight():
    ninjaTurtle.right(90)
    ninjaTurtle.forward(20)
    
def goBackwards():
    ninjaTurtle.backward(20)

fungsiList = [goRight, goStraight, goBackwards, goLeft]


for i in range(200):
    ninjaTurtle.color(random.choice(colorList))
    fungsiList[random.randrange(0,4)]()


screen = Screen()
screen.exitonclick()