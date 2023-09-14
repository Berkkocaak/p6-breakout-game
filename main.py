from turtle import *
from ball import Ball
from player import Player
from brick import Brick
from score import Score
from bonus import Bonus
import random

screen = Screen()
screen.setup(width=1000, height=1000)

score = 0
tracer(0)
player = Player()
ball = Ball()
scoreboard = Score()
bonus = Bonus((1000,1000))

positions = []


bricky = [120, 150, 180, 210]
brickx = -475

for y in bricky:
    while brickx <= 470:
        positions.append((brickx, y))
        brickx += 45
    brickx = -475

bricks = []


for x in positions:
    brick = Brick(x)
    bricks.append(brick)
update()
tracer(1)

screen.onkeypress(player.move_left, "a")
screen.onkey(player.move_left, "a")
screen.onkeypress(player.move_right, "d")
screen.onkey(player.move_right, "d")
screen.listen()

def spawn_bonus(pos):
    bonus.goto(pos)
    bonus.showturtle()
    fall_bonus()

def fall_bonus():
    if bonus.isvisible():
        bonus.fall()
        screen.ontimer(fall_bonus, 10)

def move_ball():
    global score, game_is_running

    if game_is_running:

        ball.move()

        # Check collision with bonus objects
        if bonus.ycor() < -400:
            if (player.ycor() -20 <= bonus.ycor() <= player.ycor() +20 and 
            player.xcor() -75 <= bonus.xcor() <= player.xcor() +75):
                bonus.pop(5)
                score += 5       
                scoreboard.refresh_score(score)
                screen.ontimer(bonus.clear, 2000)

        # Check ball collision with player paddle
        if ball.ycor() < -400:
            if (player.ycor() -20 <= ball.ycor() <= player.ycor() +20 and 
                player.xcor() -75 <= ball.xcor() <= player.xcor() +75 and
                ball.y_move < 0):
                ball.y_bounce()

            if ball.ycor() <= -460:
                game_is_running = False
                scoreboard.game_over(score)
                player.movespeed = 0

        bricks_copy = bricks.copy()

        # Check ball collision with bricks
        for x in bricks_copy:
            if (x.ycor() -15 <= ball.ycor() <= x.ycor() +15 and 
            x.xcor() -23 <= ball.xcor() <= x.xcor() +23):
                ball.y_bounce()
                old_x = int(x.xcor())
                old_y = int(x.ycor())
                x.goto(1000,1000)
                bricks.remove(x)
                score += 1
                scoreboard.refresh_score(score)
                if random.randint(0,10) > 1:
                    print("bonus spawned")
                    spawn_bonus((old_x,old_y))

        # Check ball collision with ceiling and bounce
        if ball.ycor() >= 490: 
            if ball.y_move > 0:
                ball.y_bounce()

        # Check ball collision with side walls and bounce
        if ball.xcor() <= -490 and ball.x_move < 0 or ball.xcor() >= 490 and ball.x_move > 0:
            ball.x_bounce()

        # Check ball drop and stop the game


        screen.ontimer(move_ball, 10)

scoreboard.start_game()

game_is_running = True

move_ball()

#def motion(event):
#    x = (event.x) -500
#    y = (event.y) -500
#    print(x,y)
#
#canvas = getcanvas()
#canvas.bind('<Motion>', motion)

screen.exitonclick()