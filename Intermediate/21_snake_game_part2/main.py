import time
from turtle import Screen

from food import Food
from score import ScoreBoard
from snake import Snake

# Define Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title('Snake Game')
screen.bgcolor('black')
screen.tracer(0)

# Define snake, score board and food
snake = Snake()
score_board = ScoreBoard()
food = Food()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # Detect colision with food:
    if snake.head.distance(food) <= 15:
        snake = snake.grow()  # Grow the snake by one piece.
        food.move()  # Change position of food.
        score_board.score()  # Increase score

    if (snake.head.xcor() > 290 or snake.head.xcor() < -290) or (snake.head.ycor() > 290 or snake.head.ycor() < -290):
        score_board.game_over()
        game_is_on = False

    for piece in snake.snake[1:]:
        if snake.head.distance(piece) <= 10:
            score_board.game_over()
            game_is_on = False


    screen.listen()
    screen.onkey(fun=snake.up,key='w')
    screen.onkey(fun=snake.down,key='s')
    screen.onkey(fun=snake.right,key='d')
    screen.onkey(fun=snake.left,key='a')

screen.exitonclick()
