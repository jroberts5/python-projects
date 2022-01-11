from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
NORTH = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()

        # Initial turtle shape
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.go_to_starting_position()


    def move(self):
        self.forward(10)
        pass

    def go_to_starting_position(self):
        self.setheading(NORTH)
        self.goto(STARTING_POSITION)
