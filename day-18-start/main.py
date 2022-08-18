import random
import turtle as t

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color


tim.shape("arrow")
tim.color("red")




#for i in range(15):
#    tim.forward(10)
#    tim.penup()
#    tim.forward(10)
#    tim.pendown()

#i = 4

#tim.forward(10)
#tim.right(360/i)
#tim.forward((10)




#i = 3
#while i < 11 :
# for color in pen_colors:
#  tim.color(color)
#  for _ in range(i):
#     tim.forward(100)
#     tim.right(360/i)

#  i+=1

#from turtle import *
#from random import *    very confusing


#import turtle as t
#timmy = t.Turtle()



#import heroes
#print(heroes.gen())
angle = [0, 90, 180, 270]
def random_heading():


    tim.pensize(10)
    tim.speed(10)


    for _ in range(200):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(angle))

i = 0
tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()