from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
    
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.seth(random.randint(225, 315))
        self.x_move = random.choice((-7, 7))
        self.y_move = random.choice((-7, 7))

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))

    def x_bounce(self):
        self.x_move *= -1

    def y_bounce(self):
        self.y_move *= -1