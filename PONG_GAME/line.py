from turtle import Turtle

class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize("5")
        self.hideturtle()
        self.penup()
        self.goto(0, 290)
        self.right(90)
        for i in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)