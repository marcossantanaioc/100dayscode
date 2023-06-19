import random
from turtle import Turtle, Screen, colormode

COLORS = ['red','orange','blue','green','purple','yellow']
RUN = False

# Screen
screen = Screen()
user_bet = screen.textinput(title='Who will win the race?',prompt='Pick a color: red, orange, blue, green, purple or yellow.')
width = 1000
height = 900
screen.setup(width=width, height=height)
print(screen.screensize())

def create_turtles(num_turtles: int=1):
    colormode(255)
    turt = Turtle()
    # Change shape
    turt.shape("turtle")  # Make it a turtle
    turt.color(COLORS[num_turtles])
    turt.shapesize(1, 1, 1)  # Shape size
    turt.speed('slow')  # Speed
    turt.width(2)
    turt.penup()

    return turt

all_turtles = []
for i in range(6):
    starting_position = ((-1 * (width-20))//2, 50)
    turt = create_turtles(i)
    if turt.fillcolor() == user_bet:
        turt.pencolor('black')
        turt.fillcolor(user_bet)
    turt.goto(starting_position[0], starting_position[1]*i)
    all_turtles.append(turt)



if user_bet:
    RUN = True

i = 0

while RUN:
    running_turtle = random.choice(all_turtles)
    running_speed = random.randint(0, 25)
    running_turtle.forward(running_speed)

    if running_turtle.xcor() >= 500:
        winning_color = running_turtle.pencolor()
        RUN = False
        if winning_color == user_bet:
            print(f"You won!")
        else:
            print(f"You lost. The winning turtle is {winning_color}. Your bet was {user_bet}.")

screen.exitonclick()
