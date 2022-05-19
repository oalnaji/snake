from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(-30, 280)
        self.write(f"SCORE: {self.score}", "center")

    def eat(self):
        self.clear()
        self.score += 1
        self.setpos(-30, 280)
        self.write(f"SCORE: {self.score}", "center")

    def gameover(self):
        self.setpos(-30, 0)
        self.write("GAME OVER", "center")