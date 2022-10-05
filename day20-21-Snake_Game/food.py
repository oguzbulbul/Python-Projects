from turtle import Turtle,Screen
import random
class Food(Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5 , 0.5)
        self.penup()
        self.color("red")
        self.speed('fastest')
        self.refresh_loc()
    
    def refresh_loc(self):
        rand_x = random.randint(-275,275)
        rand_y = random.randint(-275,275)
        self.goto(x=rand_x, y=rand_y)