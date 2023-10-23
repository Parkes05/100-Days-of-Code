# Exercise 1 - Word choice
word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
guess = input('Guess a letter: ').lower()

for letters in chosen_word:
    if (guess == letters):
        print('Right')
    else:
        print('Wrong')

# Exercise 2 - List Manipulation
print(f'\nThe chosen word is {chosen_word}')
display = []
for letters in chosen_word:
    display += '_'
print(display)

for position in range(len(chosen_word)):
    if (guess == chosen_word[position]):
        display[position] = guess
print(display)

# Exercise 3 - While Loop
print(f'\nThe chosen word is {chosen_word}')
display = []
lives = 6
for letters in range(len(chosen_word)):
    display += '_'
    
while '_' in display:
    guess = input('Guess a letter: ').lower()
    for position in range(len(chosen_word)):
        if (guess == chosen_word[position]):
            display[position] = guess
    print(display)
print ('You win')

# Exercise 6 - While loop Cont.
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(f'\nThe chosen word is {chosen_word}')
display = []
lives = 6
end_of_game = False
for letters in range(len(chosen_word)):
    display += '_'
    
while (not end_of_game == True):
    guess = input('Guess a letter: ').lower()
    for position in range(len(chosen_word)):
        if (guess == chosen_word[position]):
            display[position] = guess
    
    if guess in chosen_word:
        print(f'\n{" ".join(display)}')
    else:
        lives -= 1
        print(stages[lives])
        print(f'{" ".join(display)}')
        
    if ('_' not in display):
        end_of_game = True
        print('You Win!')
    elif (lives == 0):
        end_of_game = True
        print('You Lose')

# Project - Hangman
import sys
sys.path.append('../Data')
import hangman_art_7, hangman_words_7, random, os
def clear():
  os.system('cls')

print(hangman_art_7.logo)
chosen_word = random.choice(hangman_words_7.word_list)
display = []
lives = 6
end_of_game = False
word_length = len(chosen_word)
for word in range(word_length):
    display += '_'

while (not end_of_game == True):
    guess = input('Guess a letter: ')
    clear()
    
    if (guess in display):
        print(f'You have already guessed {guess}.')
        
    for position in range(word_length):
        if guess in chosen_word[position]:
            display[position] = guess
    print(f'\n{" ".join(display)}')      
      
    if (guess not in chosen_word):
        print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
        lives -= 1
        if lives == 0:
            print('You Lose')
            end_of_game = True      
                 
    if ('_' not in display):
        end_of_game = True
        print('You Win!')
    
    print(hangman_art_7.stages[lives])   
    
        
        
        