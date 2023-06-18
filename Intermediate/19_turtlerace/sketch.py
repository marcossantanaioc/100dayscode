import colorgram
import random
from turtle import Turtle, Screen, colormode

timmy = Turtle()
# Change shape
timmy.shape("arrow")  # Make it a turtle
timmy.shapesize(1, 1, 1)  # Shape size
timmy.speed('fastest')  # Speed
timmy.width(2)

# Initial setup
timmy.penup()
timmy.setposition(x=-200, y=-200)
timmy.pendown()
colormode(255)
# Screen
screen = Screen()

# Move functions

def clear():
    timmy.clear()
    #timmy.reset()
def move_forward():
    #timmy.setheading(0)
    return timmy.forward(10)

def move_backwards():
    #timmy.setheading(0)
    return timmy.backward(10)
#
def up():
    heading = timmy.heading() + 10
    timmy.setheading(heading)
    #return timmy.forward(10)

def down():
    heading = timmy.heading() - 10
    timmy.setheading(heading)
    #return timmy.forward(10)

screen.listen()
screen.onkey(fun=up,key='w')
screen.onkey(fun=down,key='s')
screen.onkey(fun=move_forward,key='d')
screen.onkey(fun=move_backwards,key='a')
screen.onkey(fun=clear,key='c')
screen.exitonclick()
