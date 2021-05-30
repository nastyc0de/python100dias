# import colorgram
from turtle import Turtle, Screen, colormode, dot, goto
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.speed(1)
timmy.penup()
y=-220
timmy.goto(-220,y)


colormode(255)
colors = [(57, 106, 148), (224, 201, 110), (133, 85, 59), (222, 142, 65), (196, 145, 171), (144, 179, 203), (138, 82, 105), (210, 91, 67), (187, 79, 120), (134, 182, 136), (69, 104, 89), (65, 155, 90), (133, 133, 75), (49, 155, 194), (214, 178, 191), (22, 68, 112), (21, 59, 95), (175, 202, 181), (114, 124, 150), (227, 176, 167), (158, 205, 214), (70, 59, 48), (72, 65, 53), (124, 45, 40), (110, 48, 58)]

for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(colors))
        timmy.forward(50)
    y += 50
    timmy.penup()
    timmy.goto(-220,y)   


screen = Screen()
screen.exitonclick()
# # def generate_color(num_color):
# #     path = '/Users/Andres/python100dias/dia18-Proyecto-tortuga/proyecto-Pintura-Hirst/hirst.jpg'
# #     colors = colorgram.extract(path, num_color)

# #     list_color = []
# #     for i in range(num_color):
# #         color = colors[i]
# #         rgb = color.rgb
# #         data_color = (rgb.r, rgb.g, rgb.b)
# #         list_color.append(data_color)
# #     return list_color

# # a = generate_color(30)
# # print(a)