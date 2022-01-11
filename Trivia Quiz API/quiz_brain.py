import html

class QuizBrain:
    def __init__(self, q_list):
        self.quiz_number = 0
        self.question_list = q_list
        self.score = 0
        self.current_question = None

    # Gets next question from the question bank
    def next_question(self):
        self.current_question = self.question_list[self.quiz_number]
        self.quiz_number += 1
        q_text = html.unescape(self.current_question.text)
        return f" Q.{self.quiz_number}: {q_text}"

    # Checks if there are any remaining questions left
    def is_questions_remaining(self):
        return len(self.question_list) > self.quiz_number

    # Checks player answer to the correct answer
    def check_answer(self, user_answer, correct_answer):
        print(user_answer)
        print(correct_answer)
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

