from turtle import Screen
from cars import Cars
import time
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

n = time.time()
level = 1
cars = Cars()
player = Player()
scoreboard = Scoreboard()
game_is_on = True


screen.listen()
screen.onkeypress(player.up, 'w')
screen.onkeypress(player.down, 's')


while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.move()
    current_time = time.time()

    if current_time - n > 0.3 - (cars.speed-10)*0.075:
        cars.add_new()
        n = current_time

    if player.ycor() > 260:
        level += 1
        scoreboard.increase_score()
        player.goto(0, -270)
        cars.speed += 10

    for car in cars.car_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False





screen.exitonclick()