from turtle import Turtle, Screen



screen = Screen()
pen = Turtle()
pen.color("black")
pen.penup()
pen.setposition(x=-500, y=-490)
pen.write("ohio", move=False, font=("courier", 10, "normal"))
pen.home()




screen.exitonclick()
