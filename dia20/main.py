from snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(600, 600, 200)
screen.bgcolor('black')
screen.title('SNAKE')
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
        

screen.exitonclick()