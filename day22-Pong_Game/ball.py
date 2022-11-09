from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def go_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def y_bounce(self):
        self.y_move *= -1
    def x_bounce(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0,0)
        self.x_bounce()
    

