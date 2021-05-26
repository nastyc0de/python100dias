# from turtle import Turtle, Screen
# from another_module import variable
# print(variable)
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.shapesize(10,10,10)
# timmy.color("DarkBlue")
# timmy.forward(150)
#
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Pokemon name", "Type"]
table.align = "c"
table.add_row(["Pikachu", "Electric"])
table.add_row(["Charmander", "Fire"])
table.add_row(["Squirtle", "Water"])
print(table)
