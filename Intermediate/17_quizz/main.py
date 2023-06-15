from question_model import Question
from quiz_brain import QuizzBrain
from data import question_data

question_bank = []
for qst in question_data:
    question = Question(qst)
    question_bank.append(question)

quizz = QuizzBrain(question_bank)

while quizz.still_has_questions():
    quizz.next_question()
