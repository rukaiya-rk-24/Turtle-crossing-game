from turtle import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-360,260)
        self.write(f"Level : {self.level}", align = "left", font = ("Arial",20,"normal"))
        self.color("black")
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align = "center", font = ("Arial", 20 , "normal"))


    def increase_s(self):
        self.level += 1
        self.clear()
        self.write(f"Level : {self.level}",align = "left",font = ("Arial",20,"normal"))