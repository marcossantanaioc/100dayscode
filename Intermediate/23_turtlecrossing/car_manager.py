from turtle import Turtle
import random


class CarManager:
    COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
    STARTING_MOVE_DISTANCE = 5
    MOVE_INCREMENT = 10

    def __init__(self):
        self.all_cars = []
        self.random_chance_min = 1
        self.random_chance_max = 5

    def create_car(self):
        random_chance = random.randint(self.random_chance_min, self.random_chance_max)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(self.COLORS))
            random_y = random.randint(-260, 260)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.bk(self.STARTING_MOVE_DISTANCE)

    def increase_difficulty(self):
        self.random_chance_max -= 1
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT
