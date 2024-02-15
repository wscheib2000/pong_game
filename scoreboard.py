from turtle import Turtle

SCOREBOARD_HEIGHT = 160
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.display()

    def increase_score(self, player):
        if player == 1:
            self.l_score += 1
        elif player == 2:
            self.r_score += 1
        else:
            print("ERROR: Invalid player provided to Scoreboard.increase_score()")
        self.display()

    def display(self):
        self.clear()
        self.goto(-40, SCOREBOARD_HEIGHT)
        self.write(arg=self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(40, SCOREBOARD_HEIGHT)
        self.write(arg=self.r_score, align=ALIGNMENT, font=FONT)