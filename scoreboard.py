from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.levels()

    def levels(self):
        self.clear()
        self.goto(0, 250)
        self.level += 1
        self.write(f"Level :{self.level}", align="center", font=("Courier", 24, "normal"))

    def dead(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=("Courier",  30, "normal"))
