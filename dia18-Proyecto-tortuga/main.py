
from turtle import Turtle, Screen, colormode
import random
timmy = Turtle()
timmy.shape('turtle')

colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def random_walk(n):
    turn = [0,90,180,270,360]
    colors = ['red', 'crimson','blue','green','yellow', 'salmon', 'medium blue', 'dodger blue', 'olive drab','lime green']
    inc = 1
    while inc <=n:
        aleatorio = random.choice(turn)
        timmy.right(aleatorio)
        timmy.pencolor(random_color())
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

