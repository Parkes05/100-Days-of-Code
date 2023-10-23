import sys
sys.path.append('../Data')
import os
import random
from art_14 import logo, vs
from game_data_14 import data

def clear():
    '''Clears the terminal'''
    os.system('cls')

def dictionary_to_string(list):
    '''Returns a string of the input dictonary
    without the number of followers'''
    name = list['name']
    country = list['country']
    description = list['description']
    return f'{name}, a {description}, from {country}.'

def formated_string(n1, n2):
    print(f'Compare A: {dictionary_to_string(n1)}')
    print(vs)
    print(f'Against B: {dictionary_to_string(n2)}')

clear()
print(logo)

data_1 = random.choice(data)
data_2 = random.choice(data)
if data_1 == data_2:
    data_2 = random.choice(data)

formated_string(data_1, data_2)

continue_game = True
count = 0
while continue_game:
    if data_1['follower_count'] > data_2['follower_count']:
        right_guess = data_1
    else:
        right_guess = data_2

    if input('\nWho has more followers? Type "A" or "B": ').upper() == 'A':
        player_guess = data_1['follower_count']
    else:
        player_guess = data_2['follower_count']

    if player_guess == right_guess['follower_count']:
        clear()
        print(logo)
        count += 1
        print(f'You\'re right! Current score: {count}.')
        data_1 = right_guess
        data_2 = random.choice(data)
        if data_1 == data_2:
            data_2 = random.choice(data)
        formated_string(data_1, data_2)

    else:
        clear()
        print(logo)
        print(f'Sorry, that\'s wrong. Final score: {count}.')
        continue_game = False