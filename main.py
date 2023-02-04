from turtle import *
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800,height=600)
screen.listen()
screen.tracer(0)
bib = Cars()
player = Player()
screen.onkey(key="Up",fun=player.move)
game_on = True
sis = Scoreboard()

while game_on:
    time.sleep(0.2)
    screen.update()
    bib.add_car()
    bib.move()
    if player.ycor() > 290:
        sis.increase_s()
        player.goto(0, -270)
    for i in bib.all_b:
        if player.distance(i) < 20:
            game_on = False
            sis.game_over()



















screen.exitonclick()