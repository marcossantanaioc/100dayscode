from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, shape='turtle'):
        super().__init__()
        self.penup()
        self.shapesize(0.5,0.5)
        self.color('blue')
        self.shape(shape)

        initial_x_position = random.randint(-250, 250)
        initial_y_position = random.randint(-250, 250)
        self.goto(initial_x_position, initial_y_position)

    def move(self):
        x_position = random.randint(-250, 250)
        y_position = random.randint(-250, 250)
        self.goto(x_position, y_position)
