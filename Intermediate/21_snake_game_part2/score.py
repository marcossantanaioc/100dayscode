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
        self.highest_score = 0

    def update_highest_score(self):
        if self.points > self.highest_score:
            self.highest_score = self.points
        with open('high_scores.txt', 'w') as f:
            f.write(str(self.highest_score))

    def score(self):
        self.points += 1

        self.clear()
        self.write(f"Score = {self.points}", move=False, align="center", font=(self.FONT, self.FONT_SIZE))


    def game_over(self):
        self.update_highest_score()
        self.goto(0,0)
        self.write(f"GAME OVER\nHighest Score = {self.highest_score}", move=False, align="center", font=(self.FONT, self.FONT_SIZE))

