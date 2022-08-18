# import colorgram
#
# colors = colorgram.extract("spot.jpg",25)
# color_palette = []
#
#
# for _ in range(len(colors)):
#     r = colors[_].rgb.r
#     g = colors[_].rgb.g
#     b = colors[_].rgb.b
#     color = (r,g,b)
#     color_palette.append(color)
#
# print(color_palette)
import turtle

color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61), (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39), (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202), (62, 26, 45), (145, 165, 181), (6, 79, 111)]


import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.shape("arrow")
tim.speed("slow")

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
numer_of_dots = 100


for i in range(1,numer_of_dots+1):
        tim.dot(20,random.choice(color_list))
        tim.forward(50)

        if i % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)








screen = t.Screen()
screen.exitonclick()