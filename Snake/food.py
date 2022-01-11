from turtle import Turtle
import random

COLORS = ('red', 'blue', 'orange', 'green', 'purple', 'yellow')


class Food(Turtle):

    def __init__(self):
        super().__init__()

        # Creates the food - overall shape
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.shape('circle')
        self.color(random.choice(COLORS))
        self.penup()
        self.speed('fastest')

    # Sets location of food
    def new_location(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
