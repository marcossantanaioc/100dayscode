from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")  # Make it a turtle
        self.color('white')
        self.width(20)
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.9

    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1
