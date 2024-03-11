import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

score = Scoreboard()
player = Player()
car = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    sleep_time = 0.05
    screen.update()
    time.sleep(sleep_time)

    car.create_car()
    car.move()

    for i in car.all_cars:
        if i.distance(player) < 25:
            score.dead()
            game_is_on = False

    if player.ycor() > 290:
        player.goto((0, -280))
        car.level_up()
        score.levels()


screen.exitonclick()
