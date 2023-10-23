# Exercise 1 - Odd or Even
# number = int(input("Which number do you want to check? "))
number = int(input("Which number do you want to check? "))
if number%2 == 0:
    print('This is an even number.')
else:
    print('This is an odd number.')
    
# Exercise 2 - BMI 2.0
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight / height ** 2
bmi = round(bmi)
if bmi < 18.5:
    print(f'Your BMI is {bmi}, you are underweight')
elif bmi < 25:
    print(f'Your BMI is {bmi}, you have a normal weight')
elif bmi < 30:
    print(f'Your BMI is {bmi}, you are slightly overweight')
elif bmi < 35:
    print(f'Your BMI is {bmi}, you are obese')
else:
    print(f'Your BMI is {bmi}, you are clinically obese')
    
# Exercise 3 - Leap Year
# year = int(input("Which year do you want to check? "))
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year.')
        else:
            print('Not leap year.') 
    else:
        print('Leap year.')
else:
    print('Not leap year.') 

# Exercise 4 - Pizza Order Practice
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
        bill += 1

print(f'Your final bill is: ${bill}.')

# Exercise 5 - Love Calculator 
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

words_to_count = lower_name1+lower_name2

t_count = words_to_count.count('t')
r_count = words_to_count.count('r')
u_count = words_to_count.count('u')
e_count = words_to_count.count('e')
true_count = t_count + r_count + u_count + e_count

l_count = words_to_count.count('l')
o_count = words_to_count.count('o')
v_count = words_to_count.count('v')
e_count = words_to_count.count('e')
love_count = l_count + o_count + v_count + e_count

love_score = int(f'{true_count}{love_count}')

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score > 40) and (love_score < 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

# Project - Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice1 = input('You arrive at a cross-roads, what direction do you go, "left" or "right"?: ').lower()
if choice1 == 'right':
    print('You\'re eaten by a pack of wolves. Game Over')
else:
    choice2 = input('You come across a river, do you "swim" or "wait"?: ').lower()
    if choice2 == 'swim':
        print('You\'re eaten by a crocodile. Game Over')
    else:
        choice3 = input('You are magically teleported to three door, do you choose the door with colour "red", "blue" or "yellow"?: ').lower()
        if choice3 == 'red' or choice3 == 'blue':
            print('You\'re hit with a wave of radiation and die instantly. Game Over')
        else:
            print('Congratulations, You Win!')