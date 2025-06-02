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
    
    lastPoint_x_0 = segments[0].xcor()
    lastPoint_y_0 = segments[0].ycor()
    
    lastPoint_x_1 = segments[1].xcor()
    lastPoint_y_1 = segments[1].ycor()
    
    segments[0].forward(20)
    # print(segments[0].xcor())
    # print(segments[0].ycor())        
    
    segments[1].goto(x = lastPoint_x_0, y = lastPoint_y_0)
    segments[2].goto(x = lastPoint_x_1, y = lastPoint_y_1)
    
    screen.listen()
    screen.onkey(key="w", fun=move_up)
    screen.onkey(key="s", fun=move_down)
    screen.onkey(key="a", fun=move_left)
    screen.onkey(key="d", fun=move_right)
    
screen.exitonclick()