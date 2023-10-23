# Exercise 1 - Functions
def greet():
    print('Hello')
    print('Hi')
    print('Olla')

greet()

def greet_with (name, location):
    print(f'Hello, {name}')
    print(f'What is it like in {location}')

greet_with('Chike', 'Abuja')
greet_with(name = 'Chike', location = 'Abuja')

# Exercise 2 - Paint Area Calculator
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)
import math

def paint_calc(height, width, cover):
    number_of_paint = math.ceil(height * width / cover)
    print(f'You\'ll need {number_of_paint} cans of paint.')

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# Exercise 3 - Prime Numbers
# n = int(input("Check this number: "))
# prime_checker(number=n)
def prime_checker(number):
    prime = True
    if (number != 1 or number != 2): 
        for num in range(2, number):
            if number%num == 0:
                print(f'It\'s not a prime number.')
                prime = False
                break
            
    if (prime == True):
        print(f'It\'s a prime number.') 

n = int(input("Check this number: "))
prime_checker(number=n)

# Project - Caesar Cipher
import sys
sys.path.append('../Data')
from art_8 import logo
print(logo)
choice = 'yes'

while choice == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 26
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
                'w', 'x', 'y', 'z'] * 2

    def caesar(plain_text, shift_amount, stated_direction):
        code_text = ''
        for char in plain_text:
            if char in alphabet:   
                alphabet_index = alphabet.index(char)
                if stated_direction == 'encode':
                    position = alphabet_index + shift_amount
                elif stated_direction == 'decode': 
                    position = alphabet_index - shift_amount
                code_text += alphabet[position]
            else: 
                code_text += char
        
        print(f'The {stated_direction}d text is {code_text}')
        
    caesar(plain_text = text, shift_amount = shift, stated_direction = direction)
    choice = input('Type "yes" if you want to go again. Otherwise type "no":\n')    