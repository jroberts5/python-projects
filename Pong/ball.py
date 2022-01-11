from turtle import Turtle

STARTING_X_MOVEMENT_SPEED = 15
STARTING_Y_MOVEMENT_SPEED = 15

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        # Creates the shape of the ball
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.shape('circle')
        self.color('white')
        self.penup()

        #amount of movement
        self.x_movement = STARTING_X_MOVEMENT_SPEED
        self.y_movement = STARTING_Y_MOVEMENT_SPEED

    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)

    # Reverse the x-axis movement
    def change_x_direction(self):
        self.x_movement *= -1

    # Reverse the y-axis movement
    def change_y_direction(self):
        self.y_movement *= -1

    def reset_position(self):
        self.home()
        self.change_x_direction()
        self.reset_speed()

    # Reverse the x-axis movement
    def increase_speed(self):
        if self.x_movement < 0:
            self.x_movement += -3
        if self.x_movement > 0:
            self.x_movement += 3

    def reset_speed(self):
        self.x_movement = STARTING_X_MOVEMENT_SPEED
        self.y_movement = STARTING_Y_MOVEMENT_SPEED
