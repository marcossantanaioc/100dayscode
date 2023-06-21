from turtle import Turtle


class ScoreBoard(Turtle):
    FONT = 'Courier'
    FONT_SIZE = 46

    def __init__(self, x_position: int = 200, y_position: int = 100, align: str = 'right'):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(x_position, y_position)
        self.hideturtle()
        self.points = 0
        self.align = align
        self.write(f"{self.points}", move=False, align=self.align, font=(self.FONT, self.FONT_SIZE))

    def score(self):
        self.points += 1
        self.clear()
        self.write(f"{self.points}", move=False, align=self.align, font=(self.FONT, self.FONT_SIZE))
