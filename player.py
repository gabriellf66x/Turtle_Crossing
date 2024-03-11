import random
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto((0, -280))

    def up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    STARTING_POSITION = 0
    MOVE_DISTANCE = 10
    FINISH_LINE_Y = 280
