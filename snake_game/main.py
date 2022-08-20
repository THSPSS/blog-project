from turtle import Screen
from snake import Snake
from food import Food #neme of file import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(2)    #tracer : turn turtle animation on/off and set delay for update drawings it means tracing is off?


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update() #Perform a turtlescreen update. To be used when tracer is turned off.
    time.sleep(0.2)  # suspends execution for the given number of seconds. it means stop program for 0.1 moment

    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15: #if turtle have a food, its position updated
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()


    #Detect collistion with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_is_on = False
            scoreboard.game_over()

    #if head collides with any segment in the tail:



screen.exitonclick()