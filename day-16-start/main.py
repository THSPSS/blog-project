# import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()  #Turtle is class , and timmy is name of turtle
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("pokemon Name",["Pikachu","Squirtle","charmarmand"])
table.add_column("Type",["Electric","Water","Fire"])

table.align = "l"
print(table)