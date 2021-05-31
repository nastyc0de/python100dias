from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('SNAKE')
screen.tracer(0)
start_position= [(0,0), (-20, 0),(-40, 0)]
segments = []

for position in start_position:
    new_segment = Turtle(shape='square')
    new_segment.penup()
    new_segment.color('white')
    new_segment.goto(position)
    segments.append(new_segment)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segment in range(len(segments)-1, 0, -1):
        new_x = segments[segment -1].xcor()
        new_y = segments[segment -1].ycor()
        segments[segment].goto(new_x, new_y)
        

screen.exitonclick()