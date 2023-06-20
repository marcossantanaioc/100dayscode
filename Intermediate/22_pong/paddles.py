import time
from turtle import Screen
from turtle import Turtle
from typing import List

# Define Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(0)


class Paddle:
    """
    Creates a paddle to start playing Pong.
    Attributes
    ----------
    BLOCK_SIZE
        The size of each piece of the paddle.
    NUM_SEGMENTS
        Number of pieces in the paddle.
    STARTING_POSITION
        The start position of each piece.
        Starting from the head ((0,0)),
        the other pieces are added in equal
        BLOCK_SIZE intervals.
    snake
        A list containing pieces of the paddle.
        Each piece is a square.
    head
        The first piece or head of the paddle.
        This is the part that guides the movement.
    """
    BLOCK_SIZE = 20
    #NUM_SEGMENTS = 1
    #STARTING_POSITION = [(0, 0)]

    # for segment in range(1, NUM_SEGMENTS):
    #     segment *= - 1
    #     STARTING_POSITION.append((segment * BLOCK_SIZE, 0))

    def __init__(self):
        self.paddle = self.draw_paddle()

    def draw_paddle(self) -> List[Turtle]:
        """
        Draw a snake.
        Parameters
        ----------
        num_segments
            Number of pieces in the snake.
        Returns
        -------
            The snake consists of a list
            of pieces. Each piece is a turtle object.
        """

        # whole_snake = []
        # for i in range(num_segments):
        piece = Turtle()
        piece.shape("square")  # Make it a turtle
        piece.color('white')
        piece.shapesize(1, 1, 1)  # Shape size
        piece.speed('slowest')  # Speed
        piece.width(2)
        piece.penup()
        piece.goto(x=0, y=0)
        piece.forward(0)

        #whole_snake.append(piece)

        return piece

    def move(self, distance: int = 20) -> List[Turtle]:
        # for index in range(len(self.snake) - 1, 0, -1):  # Make the tail follow the head by using negative indices
        #     new_x, new_y = self.paddle[index - 1].xcor(), self.snake[index - 1].ycor()
        #     self.snake[index].goto(new_x, new_y)
        self.paddle.forward(distance)
        return self.paddle

    def add_piece(self):
        piece = Turtle()
        piece.shape("square")  # Make it a turtle
        piece.color('white')
        piece.shapesize(1, 1, 1)  # Shape size
        piece.speed('slowest')  # Speed
        piece.width(2)
        piece.penup()
        return piece

    def up(self):
        """
        Moves the snake up.

        """
        self.paddle.setheading(90)

    def down(self):
        """
        Moves the snake down.

        """
        self.paddle.setheading(270)


paddle = Paddle()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    paddle.move()

    screen.listen()
    screen.onkey(fun=paddle.up, key='w')
    screen.onkey(fun=paddle.down, key='s')

screen.exitonclick()
