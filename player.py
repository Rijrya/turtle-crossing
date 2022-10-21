from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_new()

    def create_new(self):
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(0, -270)

    def up(self):
        cur_y = self.ycor()
        self.goto(0, cur_y + 20)

    def down(self):
        cur_y = self.ycor()
        self.goto(0, cur_y - 20)
