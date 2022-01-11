THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

SCORE_FONT = ('Arial', 14)
QUESTION_FONT = ('Arial', 16, 'italic')

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.app = Tk()
        self.app.title("Trivia Quiz Game")
        self.app.config(padx=20, pady=20, bg=THEME_COLOR)
        # Labels for scores and text
        self.score = Label(text='Score: 0', fg='white', bg=THEME_COLOR, font=SCORE_FONT)
        self.score.grid(column=0, columnspan=2, row=0, pady=20)
        # Canvas
        self.canvas = Canvas(width=300, height=250, bg='#FFFFFF', highlightthickness=0)
        self.canvas_bg = self.canvas.create_image(300, 250)
        self.canvas.grid(column=0, columnspan=2, row=1)
        self.question_text = self.canvas.create_text(150, 110, text='Enter quote here', width=250, font=QUESTION_FONT)
        # Buttons
        self.true_img = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=self.true_img, highlightthickness=0, bg=THEME_COLOR, pady=20, command=self.click_true_button)
        self.true_button.grid(column=0, row=2,pady=20)
        self.false_img = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=self.false_img, highlightthickness=0, bg=THEME_COLOR, command=self.click_false_button)
        self.false_button.grid(column=1, row=2, pady=30)
        self.get_next_question()
        self.app.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.is_questions_remaining():
            self.update_score()
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='End of Quiz')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def click_true_button(self):
        is_correct = self.quiz.check_answer("True", self.quiz.current_question.answer)
        self.give_feedback(is_correct)

    def click_false_button(self):
        is_correct = self.quiz.check_answer("False", self.quiz.current_question.answer)
        self.give_feedback(is_correct)

    def update_score(self):
        if self.quiz.score == 0 and self.quiz.quiz_number < 1:
            self.score.config(text=f"Score:{self.quiz.score}")
        else:
            self.score.config(text=f"Score:{self.quiz.score}/{self.quiz.quiz_number}")

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg='green')
        elif not is_correct:
            self.canvas.config(bg='red')
        self.app.after(1000, self.get_next_question)
