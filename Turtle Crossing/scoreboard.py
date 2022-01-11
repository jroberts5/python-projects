from turtle import Turtle

SCOREBOARD_LOCATION = (-220, 240)
FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color('white')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(SCOREBOARD_LOCATION)

    def display_level(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over.", align=ALIGNMENT, font=FONT)