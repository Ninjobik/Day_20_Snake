from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = -1
        self.setposition(0, 280)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Your Score is: {self.score}", False, "center", ("Ariel", 12, "normal"))

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", False, "center", ("Ariel", 16, "normal"))
