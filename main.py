from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

is_game_on = True

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My snake game.")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, "Left")

jackpot = 0
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect the collision of snake with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.track_score()
        snake.extend()

    # detect the collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        snake.reset_snake()
        scoreboard.reset_score()

    # detect the collision with own tail
    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset_snake()
            scoreboard.reset_score()

screen.exitonclick()
