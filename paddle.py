from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, xcor) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=0.5)
        self.penup()
        self.color("white")
        self.goto(xcor, 0)

    def up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        self.goto(self.xcor(), self.ycor()-20)