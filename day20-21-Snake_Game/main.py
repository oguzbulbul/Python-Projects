
from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from score import Score
map = Screen()
map.tracer(0)
map.title("welcome to the nostalgia ")
map.setup(width=600,height=600)
map.bgcolor("black")

snake = Snake()
food = Food()
score= Score()

map.listen()
map.onkey(fun=snake.up, key="Up")
map.onkey(fun=snake.down, key="Down")
map.onkey(fun=snake.right, key="Right")
map.onkey(fun=snake.left, key="Left")

keep_play = True
while keep_play :
    map.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15 :
        food.refresh_loc()
        snake.add_new_snake()
        score.refresh_score()

    if snake.head.xcor()>290 or snake.head.ycor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290 :
            keep_play=False
            score.game_over()

    for snake in snake.snakes[1:]:    
    
        if snake.head.distance(snake) < 10:
            keep_play = False
            score.game_over()



map.exitonclick()
