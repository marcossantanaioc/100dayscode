import turtle
import pandas as pd

data = pd.read_csv('50_states.csv')
data.set_index('state', inplace=True)

IMAGE_PATH = 'blank_states_img.gif'
FONT = ("Courier", 12, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game.")
screen.addshape(IMAGE_PATH)
screen.tracer(0)
turtle.shape(IMAGE_PATH)

game_is_on = True
guessed_states = []
while game_is_on:
    screen.update()
    answer = screen.textinput(title='Guess the state', prompt="What's another state's name?").title()

    if answer == 'Exit':
        missing_states_df = data.loc[~data.index.isin(guessed_states)]
        missing_states_df.to_csv('missing_states.csv')
        break

    if answer in data.index:
        guessed_states.append(answer)
        name = turtle.Turtle()
        name.hideturtle()
        name.penup()
        x, y = data.loc[answer].x, data.loc[answer].y
        name.goto(x=x, y=y)
        name.write(answer, font=FONT)

#screen.mainloop()
