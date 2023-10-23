from turtle import *

timmy = Turtle()
print(timmy)
timmy.shape('turtle')
timmy.color('blue')
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'l'
print(table)


# Project - Coffee Maker

from menu_16 import Menu, MenuItem
from coffee_maker_16 import CoffeeMaker
from money_machine_16 import MoneyMachine
import os

os.system('cls')

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    user_input = input(f'\nWhat would you like? {options}: ')
    if user_input == 'off':
        is_on = False
    elif user_input == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        items = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(items) and money_machine.make_payment(items.cost):
            coffee_maker.make_coffee(items)





