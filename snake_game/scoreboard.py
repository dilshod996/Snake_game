from turtle import Turtle

FONT = ("New Roman", 16, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        # self.goto(x=-20, y=270)
        self.position_title()

    def position_title(self):
        self.goto(x=-20, y=270)
        self.write(arg=f"Score: {self.score}", align="center", font=FONT)
        self.score += 1


    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="Game over", align="center", font=FONT)

    def result(self):
        self.goto(0, -30)
        self.write(arg=f"Overall score: {self.score -1 }", align="center", font=FONT)