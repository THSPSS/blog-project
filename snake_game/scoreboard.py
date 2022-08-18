from turtle import Turtle
ALIGNMENT ="center"
FONT = ("courier", 24,"normal")

class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.color("white")
        self.score =0
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=265)
        self.write(f"Score : {self.score}", False, ALIGNMENT, FONT)

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



