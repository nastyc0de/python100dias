
from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.speed('fastest')

colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

screen = Screen()
screen.exitonclick()

