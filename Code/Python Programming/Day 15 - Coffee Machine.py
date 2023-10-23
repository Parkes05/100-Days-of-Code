import sys
sys.path.append('../Data')
import os
from coffee_data_15 import MENU, resources

def clear():
    os.system('cls')

def drink_resources(drink):
    '''Takes the drink as input and return the resources required to make the drink
    as a list in the format [water, milk, coffee, cost]
    and [water, coffee, cost] for espresso'''
    if drink == 'espresso':
        water_r = MENU[drink]['ingredients']['water']
        coffee_r = MENU[drink]['ingredients']['coffee']
        cost_r = MENU[drink]['cost']
        return [water_r, coffee_r, cost_r]
    water_r = MENU[drink]['ingredients']['water']
    milk_r = MENU[drink]['ingredients']['milk']
    coffee_r = MENU[drink]['ingredients']['coffee']
    cost_r = MENU[drink]['cost']
    return [water_r, milk_r, coffee_r, cost_r]

def money_calculator(ct):
    '''Returns the total amount of money the user inserted'''
    print('Please insert coins')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    money_inserted = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    if money_inserted < ct:
        print('Sorry that\'s not enough money. Money refunded')
        return [False, 0]
    elif money_inserted == ct:
        return [True, money_inserted]
    elif money_inserted > ct:
        change = round(money_inserted - ct, 2)
        print(f'Here is ${change} in change.')
        return [True, (money_inserted - change)]

def enough_resources(drinks, water, coffee, milk):
    '''Takes the drink, water, coffee and milk resources in the machine, 
    checks if there is enough resources to make the drink and returns feedback'''
    if drinks == 'espresso':
        if water < drinks[0]:
            print('Sorry there is not enough water.')
            return False
        elif coffee < drinks[1]:
            print('Sorry there is not enough coffee.')
            return False
    if water < drinks[0]:
        print('Sorry there is not enough water.')
        return False
    elif milk < drinks[1]:
        print('Sorry there is not enough milk.')
        return False
    elif coffee < drinks[2]:
        print('Sorry there is not enough coffee.')    
        return False
    return True

clear()
turn_off_machine = False
water_resources = resources["water"]
milk_resources = resources["milk"]
coffee_resources = resources['coffee']
money_resources = 0

while not turn_off_machine:
    user_coffee_choice = input('\nWhat would you like? espresso/latte/cappuccino: ').lower()
    
    if user_coffee_choice == 'off':
        turn_off_machine = True 

    elif user_coffee_choice == 'report':
        print(f'Water: {water_resources}ml\nMilk: {milk_resources}ml\nCoffee: {coffee_resources}g\nMoney: ${round(money_resources, 2)}')
    
    elif user_coffee_choice == 'espresso' or user_coffee_choice == 'latte' or user_coffee_choice == 'cappuccino':
        materials = drink_resources(user_coffee_choice)
        if user_coffee_choice == 'espresso':
            stop = enough_resources(materials, water_resources, coffee_resources, milk_resources)

            if stop:
                cost = materials[2]
                money = money_calculator(cost)
                money_resources += money[1]

            if money[0] and stop:
                print(f'Here is your {user_coffee_choice} ☕. Enjoy!')
                water_resources -= materials[0]
                coffee_resources -= materials[1]

        elif user_coffee_choice == 'latte':
            stop = enough_resources(materials, water_resources, coffee_resources, milk_resources)
            if stop:
                cost = materials[3]
                money = money_calculator(cost)
                money_resources += money[1]

            if money[0] and stop:
                print(f'Here is your {user_coffee_choice} ☕. Enjoy!')
                water_resources -= materials[0]
                coffee_resources -= materials[2]
                milk_resources -= materials[1]

        elif user_coffee_choice == 'cappuccino':
            stop = enough_resources(materials, water_resources, coffee_resources, milk_resources)
            if stop:
                cost = materials[3]
                money = money_calculator(cost)
                money_resources += money[1]

            if money[0] and stop:
                print(f'Here is your {user_coffee_choice} ☕. Enjoy!')
                water_resources -= materials[0]
                coffee_resources -= materials[2]
                milk_resources -= materials[1]
    
    else:
        print('Invalid Input!')