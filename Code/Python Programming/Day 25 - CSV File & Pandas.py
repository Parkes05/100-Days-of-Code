## Exercise 1
with open('../Data/weather_data_25.csv', mode='r') as f:
    data = f.readlines()
print(data)


## Exercise 2
import csv

with open('../Data/weather_data_25.csv', mode='r') as f:
    data = csv.reader(f)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            int_temp = int(row[1])
            temperatures.append(int_temp)
    print(temperatures)


## Exercise 3
import pandas

data = pandas.read_csv('../Data/weather_data_25.csv')
print(type(data))
print(type(data['temp']))
print(data['temp'])

temp_list = data['temp'].to_list()

avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

average_temp = data['temp'].mean()
print(average_temp)

maximum_temp = data['temp'].max()
print(maximum_temp)

print(data['condition'])
print(data.condition)

print(data[data.temp == maximum_temp])

monday = data[data.day == 'Monday']
monday_temp = data.temp[0]
monday_temp = monday.temp[0]
monday_fahrenheit_temp = (monday_temp * 9/5) + 32
print(monday_fahrenheit_temp)


## Exercise 4
dict = {
    'students': ['Amy', 'Angela', 'James'],
    'scores': [76, 82, 56],
}
data = pandas.DataFrame(dict)
print(data)
data.to_csv('../Data/new_CSV_25.csv')


## Project 1
import pandas

COLORS = ['Gray', 'Cinnamon', 'Black']
count = []
dict = {}

squirrel_data = pandas.read_csv('../Data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_25.csv')
fur_color = squirrel_data['Primary Fur Color']
for color in COLORS:
    new_color = fur_color[fur_color == color]
    color_count = new_color.count()
    count.append(color_count)

dict = {
    'Fur Color': COLORS,
    'Count': count,
}

squirrel_output = pandas.DataFrame(dict)
squirrel_output.to_csv('../Data/squirrel_count_25.csv')


## Project 2
import turtle, pandas

PICTURE = '../Data/blank_states_img_25.gif'
TITLE = 'U.S. States Game'
FONT = ('Ariel', 10, 'normal')

screen = turtle.Screen()
screen.title(TITLE)
screen.setup(width=725, height=491)
screen.bgpic(PICTURE)

## comment the lines 97 out before removing comment from 100 and 101
# screen.addshape(PICTURE)
# turtle.shape(PICTURE)

## to get x and y values in the csv
# def mouse_click_cor(x, y):
#     print(x, y)
# turtle.onscreenclick(mouse_click_cor)
# turtle.mainloop()

states_data = pandas.read_csv('../Data/50_states_25.csv')
states_list = states_data.state.to_list()
game_is_on = True
state_count = 0

while game_is_on:
    answer_state = screen.textinput(title=f'{state_count}/50 States Correct', prompt='What\'s another state\'s name').title()
    
    if answer_state in states_list:
        state_index = states_list.index(answer_state)
        x_cor = states_data.x.get(state_index) # or x_cor = states_data.at[state_index, 'x']
        y_cor = states_data.y.get(state_index) # or y_cor = states_data.at[state_index, 'y']
        turtle.hideturtle()
        turtle.penup()
        turtle.setposition(x_cor, y_cor)
        turtle.write(arg=answer_state, align='center', font=FONT)
        state_count += 1
        states_list.pop(state_index)

    if state_count == 50:
        game_is_on = False

    if answer_state == 'Exit':
        game_is_on = False
        dict = {
            'States Missing': states_list
        }
        new_data = pandas.DataFrame(dict)
        new_data.to_csv('../Data/states_to_learn_25.csv')