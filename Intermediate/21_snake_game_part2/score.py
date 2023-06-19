from turtle import Turtle



class ScoreBoard(Turtle):
    FONT = 'Courier'
    FONT_SIZE = 20

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.points = 0

    def score(self):
        self.points += 1
        self.clear()
        self.write(f"Score = {self.points}", move=False, align="center", font=(self.FONT, self.FONT_SIZE))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=(self.FONT, self.FONT_SIZE))