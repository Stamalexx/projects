from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.paddle = Turtle()
        self.shape("circle")
        self.color("white")
        #self.shapesize(stretch_wid=20, stretch_len=20)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    def change_heading_y(self):
        self.y_move *= -1
    def change_heading_x(self):
        self.x_move *= -1
        self.move_speed *= 0.7

    def reset_ball(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.change_heading_x()


