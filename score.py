from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pu()
        self.setposition(0, 270)
        self.score = 0
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"SCORE = {self.score} ", align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
