from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0.00,280.00)
        self.score=0
        self.hideturtle()
        self.color("white")
        self.writing()

    def writing(self):
        self.clear()
        self.write(f"Your score is {self.score}", False, "center", font=("Frank", 14, "normal"))


    def increase(self):
        self.score=self.score+1
        self.writing()

