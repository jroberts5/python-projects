from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Initial Setup
screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# initial game variables
game_is_on = True

# Creates new snake & food - sets its initial position
food = Food()
food.new_location()
snake = Snake()
scoreboard = ScoreBoard()

# Key listeners
screen.listen()
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")

# Snake will keep moving across the screen
while game_is_on:
    scoreboard.display_score()
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Check if snake eats the food - then extends it's body
    if snake.head.distance(food) < 15:
        food.new_location()
        snake.extend()
        scoreboard.increase_score()
    # Check if snake hits the wall -then prompts game over
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        play_again = screen.textinput("Game Over", "Play Again?: Yes or No").lower()
        if play_again == 'no':
            game_is_on = False
            screen.bye()
        else:
            # Key listeners
            screen.listen()
            food.new_location()
            screen.onkey(snake.turn_left, "Left")
            screen.onkey(snake.turn_right, "Right")
            screen.onkey(snake.turn_up, "Up")
            screen.onkey(snake.turn_down, "Down")
            scoreboard.reset_score()
            snake.reset_snake()
            continue

    # Check if the snake hits it's tail -then prompts game over
    for part in snake.snake_body[1:]:
        if snake.head.distance(part) < 10:
            play_again = screen.textinput("Game Over", "Play Again?: Yes or No").lower()
            if play_again == 'no':
                game_is_on = False
                screen.bye()
            else:
                # Key listeners
                screen.listen()
                food.new_location()
                screen.onkey(snake.turn_left, "Left")
                screen.onkey(snake.turn_right, "Right")
                screen.onkey(snake.turn_up, "Up")
                screen.onkey(snake.turn_down, "Down")
                scoreboard.reset_score()
                snake.reset_snake()
                continue
