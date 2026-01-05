from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0.00,280.00)
        self.score=0
        self.hideturtle()
        self.color("white")
        self.highscore=0
        self.writing()


    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore=self.score
            self.score=0
        self.writing()


    def writing(self):
        self.clear()
        self.write(f"Your score {self.score} Highest score {self.highscore} ", False, "center", font=("Frank", 14, "normal"))


    def increase(self):
        self.score=self.score+1
        self.writing()

