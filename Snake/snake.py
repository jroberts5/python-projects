from turtle import Turtle

# Constant Variables
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

RESET_POSITION = (1100, 1100)

class Snake:
    def __init__(self):
        self.starting_x = 0
        self.starting_y = 0
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    # Creates snake with 3 parts - adds to the snake
    def create_snake(self):
        for _ in range(3):
            self.create_snake_part()

    # Creates new part
    def create_snake_part(self):
        self.new_snake_part = Turtle("square")
        self.new_snake_part.color("white")
        self.new_snake_part.penup()

        # Moves each x-cor back
        self.starting_x -= 20
        self.new_snake_part.goto(self.starting_x, self.starting_y)
        self.snake_body.append(self.new_snake_part)

    # Adds new part to the end of the snake's tail
    def extend(self):
        # Grabs the x & y coordinates of end of tail - create new part with those coordinates
        self.starting_x = self.snake_body[-1].xcor()
        self.starting_y = self.snake_body[-1].ycor()
        self.create_snake_part()

    # Moves the snake body from the tail to the head
    def move(self):
        # Last part goes to position of part ahead of it
        for part in range(len(self.snake_body) - 1, 0, -1):
            self.snake_part_x = self.snake_body[part - 1].xcor()
            self.snake_part_y = self.snake_body[part - 1].ycor()
            self.snake_body[part].goto(self.snake_part_x, self.snake_part_y)
        # The head of the snake moves forward - leads the rest of the tail
        self.head.forward(MOVING_DISTANCE)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset_snake(self):
        for part in self.snake_body:
            part.goto(RESET_POSITION)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]