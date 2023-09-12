from turtle import *
import time

class Score(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.penup()
        self.hideturtle()
        self.speed(0)

    def start_game(self):
        self.goto(0,0)
        count = 3
        while count > 0:
            self.clear()
            self.write(count, align="center", font=("Arial", 75, "bold"))
            count -= 1
            time.sleep(1)
        self.refresh_score(0)

    def refresh_score(self, score):
        self.goto(0,455)
        self.clear()
        self.write(score, align="center", font=("Arial", 30, "normal"))

    def game_over(self, score):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 75, "bold"))
        self.goto(0, -50)
        self.write(f"FINAL SCORE: {score}", align="center", font=("Arial", 35, "bold"))