from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)
    
    

# head= Turtle("square")
# head.color("white")
# head.penup()
# head.goto(0, 0)

# body = Turtle("square")
# body.color("white")
# body.penup()
# body.goto(-20, 0)

# tail = Turtle("square")
# tail.color("white")
# tail.penup()
# tail.goto(-40, 0)

def move_up():
    segments[0].setheading(90)
    
def move_down():
    segments[0].setheading(270)
    
def move_left():
    segments[0].setheading(180)
    
def move_right():
    segments[0].setheading(0)
    
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(1)
    
    for seg_num in range(len(segments) - 1, 0, -1):
        print(seg_num)
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    
screen.exitonclick()

