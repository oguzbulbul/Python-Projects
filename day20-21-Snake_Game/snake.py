from turtle import Turtle,Screen, position, setheading

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head=self.snakes[0]

    def create_snake(self): 
        for positionn in STARTING_POSITIONS  :   
            self.adding_snake(positionn)

    def adding_snake(self,position):
        snake=Turtle()
        snake.shape('square')
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)

    def add_new_snake(self):
        self.adding_snake(self.snakes[-1].position())         


    
    def move(self):
        for snake_numb in range(len(self.snakes)-1 , 0 , -1) :
            new_x = self.snakes[snake_numb-1].xcor()
            new_y = self.snakes[snake_numb-1].ycor()
            self.snakes[snake_numb].goto(new_x , new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP :
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT :
         self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)