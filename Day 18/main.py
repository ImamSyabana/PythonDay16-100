from turtle import Turtle, Screen
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

sidesNumber = 3
decagon = 10

colorList = ["LightSkyBlue", "LightSkyBlue1", "LightSkyBlue2", "LightSkyBlue3", 
             "LightSkyBlue4", "LightSlateBlue", "magenta", "magenta2"]

while sidesNumber < decagon:
    for x in range(sidesNumber):
        ninjaTurtle.forward(100)
        ninjaTurtle.right(360/sidesNumber)
        
    ninjaTurtle.color(colorList[sidesNumber - 3])
    sidesNumber = sidesNumber + 1
    
    
    

screen = Screen()
screen.exitonclick()