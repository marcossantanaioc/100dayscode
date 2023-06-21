import time

from ball import Ball
from board import Board
from paddles import Paddle
from score import ScoreBoard

screen = Board().draw_screen()
paddle = Paddle(x_position=380, color='red')
player1_score = ScoreBoard(x_position=150, y_position=150, align='right')
paddle2 = Paddle(x_position=-380)
player2_score = ScoreBoard(x_position=-150, y_position=150, align='left')
ball = Ball()
game_is_on = True
sleep_time = 0.01
while game_is_on:
    screen.update()
    screen.listen()
    time.sleep(sleep_time)
    ball.move()

    if ball.ycor() >= 190 or ball.ycor() <= -190:
        ball.bounce()

    if paddle2.distance(ball) <= 30 and ball.xcor() <= -360:
        ball.hit()
        sleep_time *= ball.move_speed

    elif paddle2.distance(ball) > 30 and ball.xcor() < -360:
        ball.goto(0, 0)
        sleep_time = 0.01
        player1_score.score()

    if paddle.distance(ball) <= 31 and ball.xcor() >= 360:
        ball.hit()
        sleep_time *= ball.move_speed

    elif paddle.distance(ball) > 30 and ball.xcor() > 360:
        ball.goto(0, 0)
        sleep_time = 0.01
        player2_score.score()

    screen.onkey(fun=paddle.up, key='w')
    screen.onkey(fun=paddle.down, key='s')
    screen.onkey(fun=paddle2.up, key='Up')
    screen.onkey(fun=paddle2.down, key='Down')

screen.exitonclick()
