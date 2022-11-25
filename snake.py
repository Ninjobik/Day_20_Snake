from turtle import Turtle
MOVE_DISTACE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self, length):
        self.snake_body = []
        self.length = length
        self.create_snake(length)
        self.head = self.snake_body[0]

    def create_snake(self, length):
        for n in range(self.length):
            new_square = self.add_square()
            new_square.setposition(-n * 20, 0)
            self.snake_body.append(new_square)

    def add_square(self):
        new_square = Turtle("square")
        new_square.shapesize(0.9, 0.9)
        new_square.penup()
        new_square.color("white")
        return new_square

    def move_snake(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].setposition(self.snake_body[i-1].pos())
        self.head.forward(MOVE_DISTACE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        new_s = self.add_square()
        new_s.setposition(self.snake_body[-1].pos())
        self.snake_body.append(new_s)
