from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.07)

    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.eat()
        snake.grow()

    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < - 290:
        game_on = False
        scoreboard.gameover()

    if snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < - 290:
        game_on = False
        scoreboard.gameover()

    for segments in range(1, len(snake.segments)):
        if snake.segments[0].distance(snake.segments[segments]) < 10:
            game_on = False
            scoreboard.gameover()











screen.exitonclick()