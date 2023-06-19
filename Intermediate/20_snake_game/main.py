import time
from turtle import Screen
from snake import Snake

#Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title('Snake Game')
screen.bgcolor('black')
screen.tracer(0)
snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    screen.listen()
    screen.onkey(fun=snake.up,key='w')
    screen.onkey(fun=snake.down,key='s')
    screen.onkey(fun=snake.right,key='d')
    screen.onkey(fun=snake.left,key='a')

screen.exitonclick()
