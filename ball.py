from turtle import Turtle
from random import choice

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("white")
        self.x_velocity = 0
        self.y_velocity = 0
    
    def start(self):
        self.x_velocity = choice([-5, 5])
        self.y_velocity = choice([-5, 5])

    def stop(self):
        self.x_velocity = 0
        self.y_velocity = 0

    def reset(self):
        self.goto(0,0)
        self.stop()

    def move(self):
        self.goto(self.xcor() + self.x_velocity, self.ycor() + self.y_velocity)

    def collides_with(self, paddle) -> bool:
        offset = paddle.shapesize()[1]*20 * (1 if paddle.xcor() < 0 else -1)
        return (abs(self.xcor() - (paddle.xcor()+offset)) < 5 and abs(self.ycor() - paddle.ycor()) < 25)