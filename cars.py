from turtle import Turtle
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.car_list = []
        self.create_car_list()
        self.speed = 10

    def create_car_list(self):
        for _ in range(15):
            car = Turtle(shape='square')
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(colors))
            new_x = random.randint(-300, 300)
            new_y = random.randint(-200, 200)
            car.goto(new_x, new_y)
            self.car_list.append(car)

    def move(self):
        for car in self.car_list:
            cur_x = car.xcor()
            cur_y = car.ycor()
            car.goto(cur_x-self.speed, cur_y)

    def add_new(self):
        car = Turtle(shape='square')
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(colors))
        new_x = 300
        new_y = random.randint(-200, 200)
        car.goto(new_x, new_y)
        self.car_list.append(car)
