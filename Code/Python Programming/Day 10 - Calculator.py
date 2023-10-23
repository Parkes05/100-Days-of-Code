# Exercise 1 - Days in Month
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(input_year, input_month):
    '''Takes the year and month, formats it 
    to return the number of days in the selected month'''
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = is_leap(input_year)
    if (month > 12) or (month <1):
        return 'Invalid month'
    if (leap_year) and (input_month == 2):
        return 29
    return month_days[input_month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# Project - Calculator
import sys
sys.path.append('../Data')
from art_10 import logo
import os
def clear():
    os.system('cls')

def addition(n1, n2):
    '''Adds two numbers and returns the value'''
    return n1 + n2    

def subtraction(n1, n2):
    '''Subtacts two numbers and returns the value'''
    return n1 - n2 

def multiplication(n1, n2):
    '''Multiplys two numbers and returns the value'''
    return n1 * n2 

def division(n1, n2):
    '''Divides two numbers and returns the value'''
    return n1 / n2 

calculations = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division,
}

def calculator():
    print(logo)
    first_number = float(input('What\'s the first number?: '))

    continue_calculating = True
    while continue_calculating:
        for i in calculations:
            print(i)
        operation = input('Pick an operation: ')

        next_number = float(input('What\'s the next number?: '))
        work = calculations[operation]
        result = work(first_number, next_number)

        print(f'{first_number} {operation} {next_number} = {result}\n')
        cal = input(f'Type "y" to continue calculating with {result}, or type "n" to start a new calculation, or type "s" to stop calculator: ').lower()
       
        if cal == 'y':
            first_number = result
        elif cal == 'n':
            clear()
            # Recursion, calling a function within it own definition
            calculator()
        elif cal == 's':
            continue_calculating = False

calculator()