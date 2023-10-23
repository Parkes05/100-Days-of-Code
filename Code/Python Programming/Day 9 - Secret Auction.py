# Exercise 1 - Grading Program
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if (student_scores[key] > 90):
        student_scores[key] = 'Outstanding'
    elif (student_scores[key] > 80):
        student_scores[key] = 'Exceeds Expectations'
    elif (student_scores[key] > 70): 
        student_scores[key] = 'Acceptable'
    else:
        student_scores[key] = 'Fail'
    
    student_grades[key] = student_scores[key]

print(student_grades)

# Exercise 2 - Dictionary in List
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited, num_of_visits, cities_visited):
    dictionary = {
        'country': country_visited,
        'visits': num_of_visits,
        'cities': cities_visited,
    }
    travel_log.append(dictionary)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# Project - Secret Auction
import sys
sys.path.append('../Data')
from art_9 import logo
import os

def clear():
    os.system('cls')

print(logo)
print('Welcome to the secret auction')
dictionary = {}
continue_bidding = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidders in bidding_record:
        if bidding_record[bidders] > highest_bid:
            highest_bid = bidding_record[bidders]
            winner_name = bidders
    print(f'The winner is {winner_name} with a bid of ${highest_bid}!') 

while continue_bidding:
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))
    dictionary[name] = bid

    other_bidders = input('Are there any other bidders? Type "yes" or "no": ').lower()
    if (other_bidders == 'no'):
        continue_bidding = False
        find_highest_bidder(bidding_record = dictionary)   

    else:
        clear()