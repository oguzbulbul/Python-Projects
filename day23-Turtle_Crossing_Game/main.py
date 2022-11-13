import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

level=Scoreboard()
turt=Player()
screen.listen()
screen.onkey(fun=turt.move ,key="Up")

car=CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    position_turt=(turt.xcor(), turt.ycor())
    if car.smash(pos=position_turt) == 1 :
        level.game_over()
        game_is_on = False
    
    if turt.ycor() > 260:
        turt.starting_pos()
        level.update_score()
        car.up_speed()


screen.exitonclick()
