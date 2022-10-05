from argparse import ArgumentDefaultsHelpFormatter
from turtle import Turtle


class Score(Turtle):
    def __init__(self, ):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0,270)
        self.write(arg=f"score : {self.score}", align="center", font=("Ariel", 20, "normal"))

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"score : {self.score}", align="center", font=("Ariel", 20, "normal"))
    
    def game_over(self):
        self.goto(0 , 0)
        self.write(arg="GAME OVER", align="center", font=("Ariel", 20, "normal"))