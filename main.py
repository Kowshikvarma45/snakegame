from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("skyblue")
my_screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
my_screen.listen()
my_screen.onkey(snake.up, 'Up')
my_screen.onkey(snake.down, 'Down')
my_screen.onkey(snake.right, 'Right')
my_screen.onkey(snake.left, 'Left')

is_game_on = True
score.scoree()
while is_game_on:
    my_screen.update()
    if snake.head.distance(food) < 15:
        score.scoree()
        food.go_to()                                       #detecting collisions with food
        snake.extend()
    if snake.head.xcor() > 288 or snake.head.xcor() < -288 or snake.head.ycor() > 288 or snake.head.ycor() < -288:
        score.game_over()
        is_game_on = False                                           #detecting collisions with the wall
    for segment in snake.turtles[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            is_game_on = False                                    #detecting collisions with the tail
    time.sleep(0.1)
    snake.move()


my_screen.exitonclick()