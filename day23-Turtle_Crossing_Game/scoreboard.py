from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-210,250)
        self.level=0
        self.write(arg=f"Level: {self.level}",align="center",font=FONT)
    
    def update_score(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}",align="center",font=FONT)

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.write(arg=f"Game Over",align="center",font=("Courier", 20, "normal"))
