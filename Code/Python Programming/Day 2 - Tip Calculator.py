# Exercise 1
two_digit_number = input('Type two digit number: ')
first_num = two_digit_number[0]
second_num = two_digit_number[1]
print(int(first_num) + int(second_num))

# Exercise 2 - BMI Calculator
height = input('Enter your height in m: ')
weight = input('Enter your weight in kg: ')
bmi = float(weight) / float(height) ** 2
print(int(bmi))

# Exercise 3
user_age = input('Enter your age: ')
years_left = 90 - int(user_age)
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365
print(f'You have {days_left} days, {weeks_left} weeks, and {months_left} months left.')

# Project - Tip Calculator
print('Welcome to the tip calculator')
total_bill = float(input('What was the total bill? $'))
tip_pen = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
num_people = int(input('How many people to split the bill? '))
tip_amount = total_bill * (tip_pen / 100)
total_bill += tip_amount
each_pay = total_bill / num_people
print(f'Each person should pay: ${round(each_pay, 2)}')
# To format the answer
a = round(each_pay, 2)
a = '{:.2f}'.format(a)
print(f'Each person should pay: ${a}')