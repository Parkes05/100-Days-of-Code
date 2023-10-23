# Exercise 1 - Average Height
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_of_height = 0
count = 0
for i in student_heights:
    sum_of_height += i
    count += 1
    
avgerage = round(sum_of_height/count)
print(avgerage)

# Exercise 2 - High Score
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

score = 0
for i in student_scores:
    if i > score:
        score = i

print(f'The highest score in the class is: {score}')

# Exercise 3 - Adding Even Numbers
sum = 0
for number in range(1, 101):
    if (number % 2 == 0):
        sum += number

print(sum)

# Exercise 4 - FizzBuzz
for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print('FizzBuzz')
    elif (number % 5 == 0):
        print('Buzz')
    elif (number % 3 == 0):
        print('Fizz')
    else:
        print(number)

# Project: Create a Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised: 
password = ''
for i in range(1, nr_letters + 1):
    password += random.choice(letters)

for i in range(1, nr_symbols + 1):
    password += random.choice(symbols)
        
for i in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(f'Your password is: {password}')

#Eazy Level - Order randomised: 
password_list = []
for i in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for i in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
        
for i in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)
random_password = ''
for char in password_list:
    random_password += char

print(f'Your password is: {random_password}')