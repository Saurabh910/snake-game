from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# initialise snake and food
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Allowing snake to react on pressing arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


screen.update()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move_forward()
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # Detect Collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290:
        scoreboard.gameover()
        is_game_on = False

    if snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.gameover()
        is_game_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.gameover()
            is_game_on = False

screen.exitonclick()
