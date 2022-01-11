from turtle import Turtle

# Player key commands
PLAYER_ONE_UP = 'w'
PLAYER_ONE_DOWN = 's'
PLAYER_TWO_UP = 'Up'
PLAYER_TWO_DOWN = 'Down'

# Directions

MOVING_DISTANCE = 30


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape('square')
        self.color('white')
        self.turtlesize(stretch_wid=0.5, stretch_len=10)
        self.left(90)
        self.penup()

        # Sends the paddle to the position depending on which player it is
        self.goto(position)

    def move_paddle_up(self):
        self.forward(MOVING_DISTANCE)

    def move_paddle_down(self):
        self.back(MOVING_DISTANCE)


