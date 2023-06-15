# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quizz

class QuizzBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)")
        self.check_answer(user_answer, question.answer)
        if not self.still_has_questions():
            print("You've completed the quiz!")
            print(f"Your final score is: {self.score}/{len(self.questions_list)}")

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {question_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print()
