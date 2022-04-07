from turtle import Turtle

FONT = ("New Roman", 16, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-20,270)
        # self.goto(x=-20, y=270)
        self.position_title()

    # x = -20, y = 270
    def position_title(self):
        self.clear()
        self.write(arg=f"Score: {self.score}   High score: {self.high_score}", align="center", font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.position_title()

    def increase_score(self):
        self.score += 1
        self.position_title()

    #


