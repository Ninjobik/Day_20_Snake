import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.random_y = None
        self.random_x = None
        self.shape("square")
        self.color("red")
        self.penup()
        self.shapesize(0.8, 0.8)

    def refresh(self):
        self.random_x = random.randint(-7, 7)
        self.random_y = random.randint(-7, 7)
        self.setposition(self.random_x * 40, self.random_y * 40)
