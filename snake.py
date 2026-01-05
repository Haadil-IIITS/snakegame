DIST=20
import random
POSITION = [(0, 0), (-20, 0), (-40, 0)]
colors=["white","yellow","orange","violet"]
from turtle import Turtle
class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for i in POSITION:
            self.add_segment(i)


    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            x = self.segment[i - 1].xcor()
            y = self.segment[i - 1].ycor()
            self.segment[i].goto(x, y)
        self.segment[0].forward(DIST)

    def up(self):
        if self.segment[0].heading()==270:
            pass
        else:
            self.segment[0].setheading(90)
    def down(self):
        if self.segment[0].heading()==90:
            pass
        else:
            self.segment[0].setheading(270)
    def right(self):
        if self.segment[0].heading()==180:
            pass
        else:
            self.segment[0].setheading(0)
    def left(self):
        if self.segment[0].heading()==0:
            pass
        else:
            self.segment[0].setheading(180)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def add_segment(self,i):
        new_segment = Turtle(shape="square")
        new_segment.color(random.choice(colors))
        new_segment.penup()
        new_segment.goto(i)
        new_segment.speed("slow")
        self.segment.append(new_segment)

    def reset(self):

        for i in self.segment:   #to remove the ghost snake
            i.goto(1000,1000)

        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

