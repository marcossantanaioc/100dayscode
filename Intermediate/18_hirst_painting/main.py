import colorgram
import random
from turtle import Turtle, Screen, colormode

timmy = Turtle()
# Change shape
timmy.shape("circle")  # Make it a turtle
timmy.shapesize(1, 1, 1)  # Shape size
timmy.speed('fastest')  # Speed
timmy.width(2)

# Initial setup
timmy.penup()
timmy.setposition(x=-200, y=-200)
timmy.pendown()
colormode(255)


# Extract 6 colors from an image.
def extract_colors(img_path: str, number_of_colors: int = 20):
    colors = colorgram.extract(img_path, number_of_colors)
    colors_rgb = []
    for color in colors:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.g
        colors_rgb.append((red, green, blue))
    return colors_rgb


colors_scheme = [
    (132, 166, 166), (221, 148, 148), (32, 42, 42), (199, 135, 135),
    (166, 58, 58), (141, 184, 184), (39, 105, 105), (237, 212, 212),
    (150, 59, 59), (216, 82, 82), (168, 29, 29), (235, 165, 165),
    (51, 111, 111), (35, 61, 61), (156, 33, 33), (17, 97, 97),
    (52, 44, 44), (230, 161, 161), (170, 188, 188), (57, 51, 51),
    (184, 103, 103), (32, 60, 60), (105, 126, 126), (175, 200, 200),
    (34, 151, 151), (65, 66, 66)]


for idx in range(0, 10):
    if idx % 2 == 0:
        timmy.setheading(0)
    for i in range(9):
        timmy.color(random.choice(colors_scheme))
        timmy.dot(size=20)
        timmy.penup()
        timmy.forward(50)

    timmy.dot(size=20)
    timmy.setheading(90)
    if idx != 9:
        timmy.forward(50)
        timmy.setheading(-180)

screen = Screen()
screen.exitonclick()
