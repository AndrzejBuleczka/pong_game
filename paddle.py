from turtle import Turtle


class Paddle():
    def __init__(self):
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.goto(350, 0)
        self.paddle.setheading(90)

    def move_up(self):
        self.paddle.forward(20)

    def move_down(self):
        self.paddle.backward(20)