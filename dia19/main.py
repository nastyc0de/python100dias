from turtle import Turtle, Screen, title
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400,200)
user = screen.textinput(title='Haz tu apuesta', prompt='Escoge una tortuga: ')
colors = ['red','orange','green','yellow','blue', 'purple']
all_turtles = []

def create_turtle(number_turtle):
    y = -100
    for i in range(number_turtle):
        new_turtle = Turtle(shape='turtle')
        new_turtle.penup()
        new_turtle.color(colors[i])
        new_turtle.goto(-230,y)
        y +=50
        all_turtles.append(new_turtle)
if user:
    is_race_on = True
    create_turtle(6)

while is_race_on:
    for player in all_turtles:
        if player.xcor() > 230:
            is_race_on = False
            winner = player.pencolor()
            if winner == user:
                print(f"Ganaste {winner}")
            else:
                print(f"Perdiste {winner}")
        
        rand_distance = random.randint(0,10)
        player.forward(rand_distance)

    # is_race_on = False

screen.exitonclick()