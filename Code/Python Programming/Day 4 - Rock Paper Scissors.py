# Exercise 1 - Heads or Tails
import random

random_num = random.randint(1,2)
if (random_num == 1):
    print('Heads')
else:
    print('Tails')
    
# Exercise 2 - Banker Roulette
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random
list_length = len(names) - 1
random_num = random.randint(0, list_length)
print(f'{names[random_num]} is going to buy the meal today!')

# Exercise 3 - Treasure Map
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

vertical = int(position[0])
horizontal = int(position[1])
map[horizontal-1][vertical-1] = 'x'

print(f"{row1}\n{row2}\n{row3}")

# Project - Rock Paper Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input('What do you choose? Type "0" for Rock, "1" for Paper and "2" for Scissors.\n'))
if player_choice >= 3:
    print('You typed an invalid number, You lose')
else:
    hand = [rock,paper,scissors]
    print(hand[player_choice])
    
    import random
    computer_choice = random.randint(0,2)
    print(f'Computer chose:\n{hand[computer_choice]}')

    if ([player_choice,computer_choice] == [0,0]) or ([player_choice,computer_choice] == [1,1]) or ([player_choice,computer_choice] == [2,2]):
        print('Draw')
    elif ([player_choice,computer_choice] == [0,1]) or ([player_choice,computer_choice] == [1,2]) or ([player_choice,computer_choice] == [2,0]):
        print('You lose')
    elif ([player_choice,computer_choice] == [0,2]) or ([player_choice,computer_choice] == [1,0]) or ([player_choice,computer_choice] == [2,1]):
        print('You win!')
    else: 
        print('Invalid number, you lose')