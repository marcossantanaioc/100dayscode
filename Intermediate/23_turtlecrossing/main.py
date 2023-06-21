import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import ScoreBoard

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)

# Setup game options
game_is_on = True
cars = CarManager()
player = Player()
score = ScoreBoard()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    # Check if player is hit by a car.
    for car in cars.all_cars:
        if player.distance(car) <= 15:
            score.game_over()
            game_is_on = False

    # Check if the player is at top of the screen.
    if player.ycor() >= 300:
        score.level_up()
        player.goto(x=0, y=-280)
        cars.increase_difficulty()

    screen.listen()
    screen.onkey(fun=player.up, key='w')


screen.exitonclick()
