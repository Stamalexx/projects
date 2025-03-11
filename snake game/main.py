from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

scoreboard = Score()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Socialistic Snake")

screen.tracer(0) #turns off the screen - freezes the screen

snake = Snake()

food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")





game_is_on = True
while game_is_on:
    screen.update()  # updates the screen - gia pio smooth game build
    time.sleep(0.09) #dimourgei ena delay
    snake.move()
    #detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_1()
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #detect collision of head with the body
    for segment in snake.segments[1:]: #slice - den 8eloume to 1o segment giati 8a vgalei game over
        if snake.head.distance(segment) <10:
            scoreboard.reset()
            snake.reset()



    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) <10:
    #         game_is_on = False
    #         scoreboard.game_over()



















screen.exitonclick()