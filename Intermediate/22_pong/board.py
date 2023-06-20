from turtle import Turtle, Screen

# Project breakdown
"""

paddles: write a class to handle paddles for player's 1 and 2
board: write a class to create the board.
ball: write a class to handle the ball
score: write a class to handle the score
"""


class Board:
    def __init__(self, width: int = 800, height: int = 400):
        self.width = width
        self.height = height
        self.screen = Screen()
        self.screen.setup(width=self.width, height=self.height)
        self.screen.title('Pong')
        self.screen.bgcolor('black')
        self.screen.tracer(0)

    def draw_line(self, heading: int = 90, position: int = 0):
        point = Turtle()
        point.setheading(heading)
        point.shape("square")  # Make it a turtle
        point.color('white')
        point.shapesize(0.25, 0.6, 0.25)  # Shape size
        point.width(2)
        point.penup()  # Put pen up and dont draw
        point.goto(x=0, y=position)
        return point

    def draw_screen(self):
        # Draw midline
        spacing = 20
        num_pieces = 1 + (self.height // spacing)
        pos = 0

        for _ in range(num_pieces):
            point = self.draw_line(position=pos, heading=90)
            pos += spacing
            if point.ycor() == self.height:
                for _ in range(2 * num_pieces):
                    point = self.draw_line(position=pos, heading=270)
                    pos -= spacing

        return self.screen
