from turtle import Turtle, Screen



screen = Screen()
snake = Turtle("square")
snake.color("black")
snake.speed("slow")


def up():
    snake.setheading(90)


def right():
    snake.setheading(0)


def left():
    snake.setheading(180)


def down():
    snake.setheading(270)



screen.listen()
screen.onkey(up,"w")
screen.onkey(down, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")





screen.exitonclick()
