from turtle import Turtle

SCOREBOARD_LOCATION = (0, 240)
ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.color('white')
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.goto(SCOREBOARD_LOCATION)

    def display_score(self):
        self.write(f"{self.p1_score} | {self.p2_score}", align=ALIGNMENT, font=FONT)

    def increase_p1_score(self):
        self.clear()
        self.p1_score += 1

    def increase_p2_score(self):
        self.clear()
        self.p2_score += 1
