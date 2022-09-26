
from site import USER_BASE
from question_model import Question


class QuizBrain :
    def __init__(self,quest_bank):
        self.question_number = 0 
        self.question_list = quest_bank
        self.score=0
    
    def next_quetion(self):
        quest = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {quest.text} (True/False)?")
        self.check_answer(user_answer, quest.answer)
    
    def still_has_question(self):
        if len(self.question_list) >= self.question_number :
            return True
        else :
            return False
    
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it right !")
            self.score += 1
        else :
            print("its wrong :d")
        print(f"your curent score is {self.score}/{self.question_number}")
        print("\n")
