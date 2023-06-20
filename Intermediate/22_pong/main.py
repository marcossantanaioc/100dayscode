import random

from board import Board
from paddles import Paddle
from ball import Ball
import time

screen = Board().draw_screen()
paddle = Paddle(x_position=380, color='red')
paddle2 = Paddle(x_position=-380)
ball = Ball()
game_is_on = True

while game_is_on:
    screen.update()
    screen.listen()
    time.sleep(0.01)
    ball.move()

    if ball.ycor() >= 190 or ball.ycor() <= -190:
        ball.bounce()

    if paddle2.distance(ball) <= 25 and ball.xcor() <= -360:
        ball.hit()

    elif paddle.distance(ball) <= 25 and ball.xcor() >= 360:
        ball.hit()

    screen.onkey(fun=paddle.up, key='w')
    screen.onkey(fun=paddle.down, key='s')
    screen.onkey(fun=paddle2.up, key='Up')
    screen.onkey(fun=paddle2.down, key='Down')

screen.exitonclick()
