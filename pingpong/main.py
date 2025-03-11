from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ping - PUNK")

screen.tracer(0)
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
score = Score()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")




game_is_on = True

while game_is_on:
     screen.update()  # updates the screen - gia pio smooth game build
     time.sleep(ball.move_speed) #dimourgei ena delay
     ball.move()
     #detect collision with walls (up and down)
     if ball.ycor() > 280 or ball.ycor() < -280:
         ball.change_heading_y()
     #detect collision with paddles
     if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) <50 and ball.xcor() < -320:
         ball.change_heading_x()

     #r paddle misses the ball
     if ball.xcor() > 440:
         ball.reset_ball()
         score.add_1_l()
     # l paddle misses the ball
     if ball.xcor() < -440:
        ball.reset_ball()
        score.add_1_r()












screen.exitonclick()