from turtle import *
import random

class Brick(Turtle):

    def __init__(self, pos, shape: str = "square", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.shape("square")
        self.shapesize(stretch_len=2)
        self.showturtle()
        self.penup()
        self.speed(0)
        self.goto(pos)