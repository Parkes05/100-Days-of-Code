# Project - Number Guessing Game (Global and local scope)
import os
import random
def clear():
    '''Clears the terminal'''
    os.system('cls')
logo = ''' _____                    _   _          _____           _           
|   __|_ _ ___ ___ ___   | |_| |_ ___   |   | |_ _ _____| |_ ___ ___ 
|  |  | | | -_|_ -|_ -|  |  _|   | -_|  | | | | | |     | . | -_|  _|
|_____|___|___|___|___|  |_| |_|_|___|  |_|___|___|_|_|_|___|___|_|  
'''

clear()
print(logo)
print('Welcome to the number guessing game')
print(f'I am thinking of a number between 1 and 100')
chosen_number = random.randint(1, 100)

EASY_MODE_LIVES = 10
HARD_MODE_LIVES = 5

def number_of_lives():
    diffulty = input('Choose your difficulty. Type "easy" or "hard": ').lower()
    if diffulty == 'easy':
        return EASY_MODE_LIVES
    else:
        return HARD_MODE_LIVES

turns = number_of_lives()
print(f'You have {turns} guesses with your chosen difficulty')

def compare(guess, number, lives):
    '''checks if the guessed number is too high or too low
    and returns the remainming number of guesses'''
    if lives == 1 and guess != number:
        return lives - 1
    if guess < number:
        print('Too low')
        return lives - 1
    elif guess > number:
        print('Too high')
        return lives - 1
    else:
        print(f'You guessed correctly. The answer is {number}')
        return -1

def game():
    new_live = turns
    player_guess = 0
    while player_guess != chosen_number:
        player_guess = int(input('\nGuess a number: '))
        new_live = compare(player_guess, chosen_number, new_live)
        if new_live == -1:
            player_guess != chosen_number
        elif new_live == 1:
            print(f'You have {new_live} guess reamining.')
            print('Try again')
        elif new_live > 1:
            print(f'You have {new_live} guesses reamining.')
            print('Try again')
        else:
            print('You are out of guesses. You lose!')
            player_guess = chosen_number

game()