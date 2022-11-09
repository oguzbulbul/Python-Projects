from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scorboard import Scorboard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title(titlestring="Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0)) 
ball = Ball()
scorboard = Scorboard()

screen.listen()
screen.onkey(fun= r_paddle.go_up , key= "Up")
screen.onkey(fun= r_paddle.go_down , key="Down")
screen.onkey(fun= l_paddle.go_up , key= "w")
screen.onkey(fun= l_paddle.go_down , key="s")

keep_play=True
speed = 0.08
while keep_play :
    time.sleep(speed)
    screen.update()
    ball.go_ball()
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.y_bounce()
        speed *= 0.9
        
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50 :
        ball.x_bounce()
        speed *= 0.7

    if ball.xcor() > 380 :
        ball.reset_ball()
        scorboard.l_point()
        scorboard.clear()
        scorboard.update()
    if ball.xcor() < -380 :
        ball.reset_ball()
        scorboard.r_point()
        scorboard.clear()
        scorboard.update()





screen.exitonclick()
