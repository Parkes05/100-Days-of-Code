# Exercise 1
print('Day 1 - Python Print Function')
print('The function is declared like this:')
print('print("what to print")')

# Exercise 2 - Debug
# print(Day 1 - String Manipulation")
# print("String Concatenation is done with the "+" sign.")
#   print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")
print('Day 1 - String Manipulation')
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print('New lines can be created with a backslash and n.')

# Exercise 3
print(len(input('What is your name? ')))

# Exercise 4 - Don't Change
# a = input("a: ")
# b = input("b: ")
# "Code"
# print("a: " + a)
# print("b: " + b)
a = input("a: ")
b = input("b: ")
a1 = a
a = b
b = a1
print("a: " + a)
print("b: " + b)

# Project - Band Name Generator
print('Welcome to the Band Name Generator.')
city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("What's your pet's name\n")
print('Your band name could be ' + city_name + ' ' + pet_name)