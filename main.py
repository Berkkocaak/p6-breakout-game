from turtle import *
from ball import Ball
from player import Player
import math

screen = Screen()
screen.setup(width=1000, height=1000)

player = Player()
ball = Ball()

player_speed = 15


screen.onkeypress(player.move_left, "a")
screen.onkey(player.move_left, "a")
screen.onkeypress(player.move_right, "d")
screen.onkey(player.move_right, "d")
screen.listen()


def move_ball():
    ball.move()
    screen.ontimer(move_ball, 5)

    # Check collision with player paddle
    if (player.ycor() -20 <= ball.ycor() <= player.ycor() +20 and 
        player.xcor() -75 <= ball.xcor() <= player.xcor() +75):
        ball.y_bounce()
    
    
    # Check collision with ceiling
    if ball.ycor() >= 490:
        ball.y_bounce()


    # Check collision with side walls
    if ball.xcor() <= -490 or ball.xcor() >= 490:
        ball.x_bounce()

move_ball()

screen.exitonclick()






## Get current mouse position's x value
## and store it as "mouse_x"
#
#mouse_x = 0
#
#def motion(event):
#    global mouse_x
#    delay(10)
#    x = (event.x)-500
#    mouse_x = x
#
#canvas = getcanvas()
#canvas.bind('<Motion>', motion)
#
## Main game_loop that moves the player and
## the ball
#
#game_is_running = True
#
#while game_is_running:
#    if mouse_x > player.xcor():
#        player.motion(heading=0, mouse_x=mouse_x)
#    else:
#        player.motion(heading=180, mouse_x=mouse_x)
#
#    update()