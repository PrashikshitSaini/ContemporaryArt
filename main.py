import turtle

import colorgram
from turtle import Turtle,Screen
import random

# mix_color = []
# colors = colorgram.extract('yep.jpg', 30)
#
#
# for colour in colors:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_color = (r, g, b)
#     mix_color.append(new_color)
# print(mix_color)
tim = Turtle()


tim.speed("fastest")
color_list = [(211, 154, 34), (218, 161, 98), (104, 252, 138), (187, 66, 11), (173, 7, 20), (219, 215, 232), (25, 2, 244), (80, 127, 189), (240, 53, 193), (241, 1, 0), (247, 243, 31), (3, 153, 3), (4, 201, 102), (254, 245, 0), (96, 3, 254), (217, 145, 155), (24, 55, 93), (3, 175, 238), (147, 204, 221), (114, 158, 204), (77, 112, 164), (118, 202, 112), (176, 53, 86), (237, 161, 195), (180, 170, 235), (214, 75, 62), (240, 166, 158)]
turtle.colormode(255)
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

dot_count = 100
for step in range(1, dot_count + 1):
    tim.dot(15, random.choice(color_list))
    tim.forward(50)


    if step % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)






Screen().exitonclick()