#from turtle import Turtle,Screen
# turtle1=Turtle()
# board=Screen()

# board.listen()
# def move_forward():
#     turtle1.forward(25)
# def move_back():
#     turtle1.setheading(180)
#     turtle1.forward(25)
# def turn_clock():
#     turtle1.right(25)
# def antiturn_clock():
#     turtle1.left(25)
# def clear_all():
#     board.clearscreen()

# board.onkey(key="w",fun=move_forward)
# board.onkey(key="s",fun=move_back)
# board.onkey(key="d",fun=turn_clock)
# board.onkey(key="a",fun=antiturn_clock),
# board.onkey(key="c",fun=clear_all)

# board.exitonclick()



import random
from turtle import Turtle,Screen
screen=Screen()
colors=["red","orange","yellow","green","blue","purple"]
screen.setup(width=750,height=600)
user_bet=screen.textinput(title="Make your bet !",prompt="Which turtle ig going to win? enter a color")
#-375 +375
turt1 = Turtle()
turt2 = Turtle()
turt3 = Turtle()
turt4 = Turtle()
turt5 = Turtle()
turt6 = Turtle()
turtles=[turt1,turt2,turt3,turt4,turt5,turt6]

def def_and_rotate(turtles):
    for temp in range(6):
        turtles[temp].penup()
        turtles[temp].color(colors[temp])
        turtles[temp].shape("turtle")
        turtles[temp].goto(x=-300, y=100 - temp*40)

def_and_rotate(turtles=turtles)
screen.title(titlestring="omg lets begin!!")

keep_race = False
if user_bet :
    keep_race = True

while keep_race :
     
     for turt in turtles :
        if turt.xcor() > 350 :
            keep_race= False
            winning_turtle = turt.pencolor()
            if winning_turtle == user_bet:
                print(f"Yeah you won! {winning_turtle} turtle is winner ")
            else :
                print(f"You lost :(  {winning_turtle} turtle is winner")
        
        go_random=random.randint(1,12)
        turt.forward(go_random)

screen.exitonclick()