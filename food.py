from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.up()
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-245, 245)
        y_cor = random.randint(-245, 245)
        self.goto(x_cor, y_cor)
