from turtle import Turtle

score_board_x = 0
score_board_y = 270
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        # Creates the scoreboard shape
        self.penup()
        self.speed('fastest')
        self.color('white')
        self.hideturtle()
        self.score = 0
        with open('high_score.txt') as current_high_score:
            self.high_score = int(current_high_score.read())
        self.goto(score_board_x, score_board_y)

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} |  High Score: {self.high_score} ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.display_score()

    def change_high_score(self):
        with open('high_score.txt', mode='w') as new_high_score:
            self.high_score = self.score
            new_high_score.write(f'{self.high_score}')

    def reset_score(self):
        if self.score > self.high_score:
            self.change_high_score()
        self.score = 0
        self.display_score()


