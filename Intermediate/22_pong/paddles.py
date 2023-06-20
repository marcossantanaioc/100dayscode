from turtle import Screen, Turtle

# Define Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(0)


class Paddle(Turtle):
    """
    Creates a snake to start playing Snake Game.

    """

    def __init__(self, x_position: int = 280):
        super().__init__()
        self.shape("square")  # Make it a turtle
        self.color('white')
        self.shapesize(1, 3, 1)  # Shape size
        self.speed('slow')  # Speed
        self.width(20)
        self.penup()
        self.setheading(90)
        self.goto(x=x_position, y=0)

    def up(self):
        """
        Moves the snake up.

        """
        self.setheading(90)
        self.forward(50)
        if self.ycor() >= 300:
            self.goto(x=self.xcor(), y=270)

    def down(self):
        """
        Moves the snake down.

        """
        self.setheading(270)
        self.forward(50)
        if self.ycor() <= -300:
            self.goto(x=self.xcor(), y=-260)
