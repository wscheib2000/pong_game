from turtle import Turtle

STEP = 10

class Board:

    def __init__(self) -> None:
        center_line = Turtle()
        center_line.penup()
        center_line.goto(0,350)
        center_line.right(90)
        center_line.pensize(3)
        center_line.pendown()
        center_line.color("white")
        for i in range(700//STEP*2):
            center_line.forward(STEP)
            center_line.penup()
            center_line.forward(STEP)
            center_line.pendown()