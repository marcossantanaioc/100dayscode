import random
from turtle import Turtle, Screen, colormode

timmy = Turtle()
colormode(255)

# Colors library
colors = ['chartreuse', 'red', 'black',
          'pink', 'cyan', 'magenta',
          'coral', 'dark olive green',
          'light steel blue','yellow']

def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return (r, g, b)

# Change shape
timmy.shape("arrow")  # Make it a turtle
timmy.shapesize(1, 1, 1)  # Shape size
timmy.speed('fast')  # Speed
timmy.width(1.5)


# Create a square
def make_square(size: int):
    timmy.forward(size)
    timmy.left(90)
    timmy.forward(size)
    timmy.left(90)
    timmy.forward(size)
    timmy.left(90)
    timmy.forward(size)


# Generalize to make regular polygons
def make_polygon(sides: int = 4, size: int = 100, angle: float = 90):
    for i in range(sides):
        timmy.forward(size)
        timmy.right(angle)


# Random walk
def random_walk():
    actions = ['forward', 'backward', 'right', 'left']
    color = random.choice(colors)
    action = random.choice(actions)
    distances = 30#random.choice(range(50, 100))
    angles = random.choice(range(-361, 361))
    if action == 'forward':
        timmy.color(color)
        timmy.forward(distances)
    elif action == 'backward':
        timmy.color(color)
        timmy.backward(distances)
    elif action == 'left':
        timmy.color(color)
        timmy.left(angles)
    else:
        timmy.color(color)
        timmy.right(angles)


# Dashed line
def dashed_line():
    timmy.forward(25)
    timmy.penup()  # Put pen up and dont draw
    timmy.forward(25)
    timmy.pendown()  # Put pen down to draw


# Overlaid shapes
#sides = list(range(3, 11))

# for index, side in enumerate(sides):
#     angle = 360 / side
#     size = 100
#     timmy.color(colors[index])
#     make_polygon(sides=side, angle=angle, size=size)

# Spirograph
# RUN = True
# while RUN:
#     timmy.circle(radius=100)
#     timmy.color(random_color())
#     timmy.tilt(60)
#     timmy.right(10)

screen = Screen()
screen.exitonclick()
