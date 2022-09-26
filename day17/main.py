from random import randint
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for question in question_data :
    que= Question(question["text"],question["answer"])
    question_bank.append(que)

quiz = QuizBrain(question_bank)
quiz.next_quetion()

while quiz.still_has_question() :
    quiz.next_quetion()

print("You completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")