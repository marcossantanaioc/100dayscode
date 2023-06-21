from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color('black')
        self.setheading(90)
        self.goto(x=0, y=-280)

    def up(self):
        """
        Moves the turtle up.

        """
        self.forward(10)
