from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align='center', font=('Arial', 24, 'normal'))
    def increase_score(self):
        self.update_score()
        self.score += 1