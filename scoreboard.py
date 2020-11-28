from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0

    def update_score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def gain_score(self):
        self.score += 1

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over \n Score is {self.score}", align="center", font=FONT)