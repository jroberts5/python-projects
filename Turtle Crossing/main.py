import time
from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard


# Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

# Game variables
GOAL = 270
player = Player()
scoreboard = Scoreboard()
game_is_on = True
cars = Car()
cars_distance = []
scoreboard = Scoreboard()


# Turtle moves forward when pressing the up key
screen.listen()
screen.onkeypress(player.move, 'Up')


while game_is_on:

    scoreboard.display_level()
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    # Checks if player reaches the goal - resets position and changes level
    if player.ycor() >= GOAL:
        player.go_to_starting_position()
        cars.next_level()
        scoreboard.increase_level()

    # Checks if the player hits one of the cars - Game over
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()











# Cars are randomly generated along the y-axis and moves across the x-axis

# Detect when the turtle collides with a car - initiates game over

# Detect when the turtle has reached the top edge of the screen (Finish_line)

# Send the turtle to the starting position

# After the turtle is sent back home, increase the speed of the cars

# Create scoreboard that keeps track of the level that the player is on in the game


screen.exitonclick()