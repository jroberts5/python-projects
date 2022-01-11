from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


# Creates the screen
screen = Screen()
screen.title("Pong")
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

# Set distance to each part of the game
TOP_WALL = 285
BOTTOM_WALL = -285
PLAYER_ONE_GOAL = -380
PLAYER_TWO_GOAL = 380

# Initial positions for both players
PLAYER_ONE_POSITION = (-350, 0)
PLAYER_TWO_POSITION = (350, 0)

# Creates the Paddles for both player one and player two
player_1_paddle = Paddle(position=PLAYER_ONE_POSITION)
player_2_paddle = Paddle(position=PLAYER_TWO_POSITION)
ball = Ball()
scoreboard = ScoreBoard()

# Key listeners for players paddles
screen.listen()
screen.onkeypress(player_1_paddle.move_paddle_up, "w")
screen.onkeypress(player_1_paddle.move_paddle_down, "s")
screen.onkeypress(player_2_paddle.move_paddle_up, "Up")
screen.onkeypress(player_2_paddle.move_paddle_down, "Down")

game_running = True

while game_running:
    scoreboard.display_score()
    time.sleep(0.1)
    screen.update()
    ball.move()
    ball.heading()


    # Checks if snake hits the wall -then bounces the ball off it
    if ball.ycor() > TOP_WALL or ball.ycor() < BOTTOM_WALL:
        ball.change_y_direction()

    # Checks if the ball hits either paddle - bounces ball off
    if ball.distance(player_1_paddle) < 60 and ball.xcor() < -330:
        ball.change_x_direction()
        ball.increase_speed()
    if ball.distance(player_2_paddle) < 60 and ball.xcor() > 330:
        ball.change_x_direction()
        ball.increase_speed()

    # Checks if the ball passes the goal for either player.

    if ball.xcor() < PLAYER_ONE_GOAL:
        ball.reset_position()
        scoreboard.increase_p1_score()
    if ball.xcor() > PLAYER_TWO_GOAL:
        ball.reset_position()
        scoreboard.increase_p2_score()






screen.exitonclick()