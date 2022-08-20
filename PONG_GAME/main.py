from turtle import Screen
from paddle import Paddle
from line import Line
from pong import Pong
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)  # turn off the tracer

line = Line()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

pong = Pong()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(pong.move_speed)
    screen.update()  # Perform a turtlescreen update. To be used when tracer is turned off.
    pong.move()



    #Detect collision with wall
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y()

    #Detect collision with r_paddle
    if pong.distance(r_paddle) < 50 and pong.xcor() > 320 or pong.distance(l_paddle) < 50 and pong.xcor() < -320:
        pong.bounce_x()

    #Detect when paddle misses
    if pong.xcor() > 380:
        pong.reset_position()
        scoreboard.l_point()

    if pong.xcor() < -380:
        pong.reset_position()
        scoreboard.r_point()


screen.exitonclick()
