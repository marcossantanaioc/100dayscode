from turtle import Turtle
from typing import List


class Snake:
    """
    Creates a snake to start playing Snake Game.
    Attributes
    ----------
    BLOCK_SIZE
        The size of each piece of the snake.
    NUM_SEGMENTS
        Number of pieces in the snake.
    STARTING_POSITION
        The start position of each piece.
        Starting from the head ((0,0)),
        the other pieces are added in equal
        BLOCK_SIZE intervals.
    snake
        A list containing pieces of the snake.
        Each piece is a square.
    head
        The first piece or head of the snake.
        This is the part that guides the movement.
    """
    BLOCK_SIZE = 20
    NUM_SEGMENTS = 3
    STARTING_POSITION = [(0, 0)]

    for segment in range(1, NUM_SEGMENTS):
        segment *= - 1
        STARTING_POSITION.append((segment * BLOCK_SIZE, 0))

    def __init__(self):
        self.snake = self.draw_snake(num_segments=self.NUM_SEGMENTS)
        self.head = self.snake[0]


    def draw_snake(self, num_segments: int) -> List[Turtle]:
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

        whole_snake = []
        for i in range(num_segments):
            piece = Turtle()
            piece.shape("square")  # Make it a turtle
            piece.color('white')
            piece.shapesize(1, 1, 1)  # Shape size
            piece.speed('slowest')  # Speed
            piece.width(2)
            piece.penup()
            piece.goto(x=self.STARTING_POSITION[i][0], y=self.STARTING_POSITION[i][1])

            whole_snake.append(piece)

        return whole_snake

    def move(self, distance: int=20) -> List[Turtle]:
        for index in range(len(self.snake) - 1, 0, -1):  # Make the tail follow the head by using negative indices
            new_x, new_y = self.snake[index - 1].xcor(), self.snake[index - 1].ycor()
            self.snake[index].goto(new_x, new_y)
        self.head.forward(distance)
        return self.snake

    def up(self):
        """
        Moves the snake up.

        """
        if self.head.heading() != 270:  # The condition avoid moving down if already moving up.
            self.head.setheading(90)

    def down(self):
        """
        Moves the snake down.

        """
        if self.head.heading() != 90:  # The condition avoid moving up if already moving down.
            self.head.setheading(270)

    def right(self):
        """
        Moves the snake right.

        """
        if self.head.heading() != 180:  # The condition avoid moving left if already moving right.
            self.head.setheading(0)

    def left(self):
        """
        Moves the snake left.

        """
        if self.head.heading() != 0:  # The condition avoid moving right if already moving left.
            self.head.setheading(180)



