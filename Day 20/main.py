from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


head= Turtle("square")
head.color("white")
head.penup()
head.goto(0, 0)

body = Turtle("square")
body.color("white")
body.penup()
body.goto(-20, 0)

tail = Turtle("square")
tail.color("white")
tail.penup()
tail.goto(-40, 0)


screen.exitonclick()