from turtle import Screen
import snake
import time
import food
import scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.title("Snake by Ninjobik")
screen.bgcolor("black")

snake = snake.Snake(10)
food = food.Food()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
scoreboard.update_score()
food.refresh()

while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move_snake()
    if snake.head.distance(food) < 10:
        food.refresh()
        scoreboard.update_score()
        snake.grow()

    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_on = False
        scoreboard.game_over()

    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
