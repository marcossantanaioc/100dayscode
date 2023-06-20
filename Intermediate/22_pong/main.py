from board import Board
from paddles import Paddle

screen = Board().draw_screen()
paddle = Paddle(x_position=270)
paddle2 = Paddle(x_position=-270)

game_is_on = True

while game_is_on:
    screen.update()
    screen.listen()

    screen.onkey(fun=paddle.up, key='w')
    screen.onkey(fun=paddle.down, key='s')
    screen.onkey(fun=paddle2.up, key='Up')
    screen.onkey(fun=paddle2.down, key='Down')

screen.exitonclick()
