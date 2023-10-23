# # Exercise 1
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = 'Angela'
new_list = [l for l in name]
print(new_list)

range_list = [num * 2 for num in range(1, 5)]
print(range_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [n.upper() for n in names if len(n) > 5]
print(long_names)


# # Exercise 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)

numbers_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers_1 if n % 2 == 0]
print(result)

with open('../Data/file1_26.txt') as f:
    num_1 = f.readlines()
    # numbers_2 = [int(n.strip()) for n in num_1]
with open('../Data/file2_26.txt') as f:
    num_2 = f.readlines()
    # numbers_3 = [int(n.strip()) for n in num_2]
result_1 = [int(n) for n in num_1 if n in num_2]
print(result_1)


# # Exercise 3
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
import random
students_scores = {students:random.randint(1, 100) for students in names}
print(students_scores)

passed_students = {name:score for (name, score) in students_scores.items() if score >= 60}
print(passed_students)

sentence = 'What is the Airspeed Velocity of an Unladen Swallow?'
result = {word:len(word) for word in sentence.split(' ')}
print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)


# # Exercise 4
student_dict = {
    'student': ['Angela', 'James', 'Lilly'],
    'score': [56, 76, 98],
    }
for (key, value) in student_dict.items():
    print(value)

import pandas
student_data = pandas.DataFrame(student_dict)
print(student_data)
for (index, row) in student_data.iterrows():
    if row.student == 'Angela':
        print(row.score)


# # Project
import pandas

data = pandas.read_csv('../Data/nato_phonetic_alphabet_26.csv')
nato_alphabet_dict = {row.letter:row.code for (index, row) in data.iterrows()}

user_input = input('Enter a word: ').upper()
code_list = [nato_alphabet_dict[letter] for letter in user_input]
print(code_list)
