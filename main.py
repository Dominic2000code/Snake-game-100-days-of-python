from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()


def quit_game():
    global game_is_on
    game_is_on = False


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(quit_game, "q")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.grow_snake()
    # Detect collision with all
    if (snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280
            or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280):
        score_board.reset_scoreboard()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            score_board.reset_scoreboard()
            snake.reset_snake()
