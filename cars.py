from turtle import *
import random
COLORS = ["red", "green", "blue", "yellow", "orange"]

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.all_b = []

    def add_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1,stretch_len=2)
        new_car.penup()
        new_car.clr = random.choice(COLORS)
        new_car.color(new_car.clr)
        new_car.pos = random.randint(-400, 400)
        new_car.goto(380, new_car.pos)
        new_car.setheading(180)
        self.all_b.append(new_car)

    def move(self):
        for i in self.all_b:
            i.forward(20)