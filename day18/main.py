"""       HIRST PAINTING      """
from turtle import Turtle,Screen,colormode
import random
#import colorgram 
# colorrs = colorgram.extract('day18/resimim.jpg', 30)
# rgb_colors = []
# for color in colorrs :
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
# comment short cut  :  Ctrl + K + C

color_list = [(232, 233, 237), (234, 238, 236), (209, 154, 66), (240, 233, 237), (40, 86, 170), (104, 160, 207), (228, 200, 58), (180, 62, 100), (147, 20, 59), (198, 117, 156), (187, 73, 40), (140, 181, 12), (52, 110, 95), (64, 54, 42), (11, 67, 136), (58, 53, 67), (180, 86, 108), (221, 175, 192), (142, 171, 165), (59, 53, 63), (104, 118, 161), (173, 188, 219), (173, 107, 95), (227, 176, 168), (69, 64, 54), (106, 140, 134), (175, 201, 197), (101, 48, 47), (162, 201, 219)]

artist_turtle = Turtle()
artist_turtle.penup()
artist_turtle.hideturtle() 
colormode(255)
artist_turtle.speed('fastest')

artist_turtle.setheading(225)
artist_turtle.forward(300)
artist_turtle.setheading(0)

def rows(row_lenght):
    for _ in range(row_lenght):
        artist_turtle.dot(20,random.choice(color_list))
        artist_turtle.forward(50)

    artist_turtle.right(180)
    artist_turtle.forward(50*row_lenght)
    artist_turtle.right(90)
    artist_turtle.forward(50)
    artist_turtle.right(90)

for _ in range(10):
    rows(10)

canvas = Screen()
canvas.exitonclick()