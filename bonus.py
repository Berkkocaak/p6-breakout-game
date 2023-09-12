from turtle import *
import random

class Bonus(Turtle):
    def __init__(self, position, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.shape("turtle")
        self.color(random.choice(("red", "green", "blue")))
        self.speed(0)
        self.seth(270)
        self.penup()
        self.goto((position))
        self.movespeed = 4
        self.hideturtle()
        
    def fall(self):
        self.sety(self.ycor() - self.movespeed)

    def pop(self, points):
        self.write(f"+{points}", align="center", font=("Arial", 20, "normal"))
        self.goto(1000,1000)