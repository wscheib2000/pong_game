from turtle import Screen
import time
from board import Board
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

board = Board()
ball = Ball()
l_paddle = Paddle(-270)
r_paddle = Paddle(270)
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=ball.start, key="space")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)

    if ball.ycor() > 190 or ball.ycor() < -180:
        ball.y_velocity *= -1

    if ball.collides_with(l_paddle) or ball.collides_with(r_paddle):
        ball.x_velocity *= -1

    if ball.xcor() > 300:
        scoreboard.increase_score(player=1)
        ball.reset()
    if ball.xcor() < -300:
        scoreboard.increase_score(player=2)
        ball.reset()
    
    ball.move()

screen.exitonclick()