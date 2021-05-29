
from turtle import Turtle, Screen, radians
import random
timmy = Turtle()
timmy.shape('turtle')


def random_walk(n):
    turn = [0,90,180,270,360]
    colors = ['red', 'crimson','blue','green','yellow', 'salmon', 'medium blue', 'dodger blue', 'olive drab','lime green']
    inc = 1
    while inc <=n:
        aleatorio = random.choice(turn)
        rand_color = random.choice(colors)
        timmy.right(aleatorio)
        timmy.pencolor(rand_color)
        timmy.forward(15)
        inc +=1

def turtle_draw(n):
    inc = 3
    while inc <= n:
        for _ in range(inc):
            timmy.right(360/inc)
            timmy.forward(100)
        inc +=1

# turtle_draw(5)
random_walk(200)
screen = Screen()
screen.exitonclick()

