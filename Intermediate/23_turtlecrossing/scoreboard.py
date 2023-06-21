from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(0, 250)
        self.write(f"Level: {self.level}", move=False, align='center', font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", move=False, align='center', font=FONT)

    def game_over(self):
        self.showturtle()
        self.goto(0, 0)
        self.write("*SQUISH*\nGame Over", move=False, align='center', font=FONT)
