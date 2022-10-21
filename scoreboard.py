from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.ht()
        self.penup()
        self.sety(260)
        self.setx(-260)
        self.increase_score()

    def game_over(self):
        self.sety(0)
        self.write("GAME OVER", align="center", font=('Courier', 20, 'normal'))

    def increase_score(self):
        self.clear()
        self.write(f"Level: {self.score}", False, align="left", font=('Courier', 20, 'normal'))
        self.score += 1
