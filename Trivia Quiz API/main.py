from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
questions_remaining = True

# Gets questions from question data and add to the question bank
for q in question_data:
    question = Question(q["question"], q["correct_answer"])
    question_bank.append(question)

# Creates the quiz with the question bank
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# The Quiz runs while there are questions left in the bank
# while questions_remaining:
#     quiz.next_question()
#     questions_remaining = QuizBrain.is_questions_remaining(quiz)
