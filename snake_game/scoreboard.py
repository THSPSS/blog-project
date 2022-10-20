from turtle import Turtle
ALIGNMENT ="center"
FONT = ("courier", 24,"normal")

class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.color("white")
        self.score =0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score} ", False, ALIGNMENT, FONT)

    def write_high_score(self):
        with open("data.txt", mode="a") as data:
            data.write(self.high_score)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score= 0
        self.update_scoreboard()
        self.write_high_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



