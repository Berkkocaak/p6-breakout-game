from turtle import Turtle

class Player(Turtle):
    def __init__(self, shape: str = "square", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shapesize(stretch_len=7)
        self.penup()
        self.speed(0)
        self.goto(0,-450)

    def move_left(self):
        if self.xcor() > -480:
            new_x = self.xcor() -20
            self.goto((new_x, self.ycor()))

    def move_right(self):
        if self.xcor() < 480:
            new_x = self.xcor() +20
            self.goto((new_x, self.ycor()))