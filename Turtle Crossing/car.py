from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SPEED_INCREMENT = 10
STARTING_SPEED = 5

# Limits and directions for car
TOP_SCREEN_LIMIT = 230
BOTTOM_SCREEN_LIMIT = -210
STARTING_EDGE = 280
WEST = 180

class Car:
    def __init__(self):
        #Initial shape for car
        self.all_cars = []
        self.cars_speed = STARTING_SPEED

    def create_car(self):
        random_chance = random.randint(0, 5)

        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(WEST)

            # Sets car in random y-location between the top and bottom limit
            new_car.starting_y_position = random.randint(BOTTOM_SCREEN_LIMIT, TOP_SCREEN_LIMIT)
            new_car.goto(STARTING_EDGE, new_car.starting_y_position)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.cars_speed)

    def next_level(self):
        self.cars_speed += SPEED_INCREMENT