from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.colors = ["red", "yellow", "orange", "green", "blue", "aquamarine", "purple"]
        self.color(random.choice(self.colors))
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.color(random.choice(self.colors))
        self.goto(random_x, random_y)
