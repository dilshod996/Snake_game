from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
# score.score_title()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()

        # scoreboard.score +=1
        # scoreboard.position()

        scoreboard.clear()
        scoreboard.position_title()
        snake.extend_snake()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        scoreboard.result()
    for part in snake.all_snakes[1:]:
        # if part == snake.head:
        #     pass
        if snake.head.distance(part) < 10:
            game_is_on = False
            scoreboard.game_over()
            scoreboard.result()

screen.exitonclick()
