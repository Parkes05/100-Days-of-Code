# #Exercise 1: Catch the exception and make sure the code runs without crashing.
# # fruits = ["Apple", "Pear", "Orange"]

# # def make_pie(index):
# #     fruit = fruits[index]
# #     print(fruit + " pie")

# # make_pie(4)
# fruits = ["Apple", "Pear", "Orange"]

# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError as error_message:
#         print(error_message)
#         print('Fruit pie')
#     else:   
#         print(fruit + " pie")

# make_pie(4)


# #Exercise 2: Catch the exception and make sure the code runs without crashing.
# # facebook_posts = [
# #     {'Likes': 21, 'Comments': 2}, 
# #     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
# #     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
# #     {'Comments': 4, 'Shares': 2}, 
# #     {'Comments': 1, 'Shares': 1}, 
# #     {'Likes': 19, 'Comments': 3}
# # ]
# # total_likes = 0

# # for post in facebook_posts:
# #     total_likes = total_likes + post['Likes']

# # print(total_likes)
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2}, 
#     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#     {'Comments': 4, 'Shares': 2}, 
#     {'Comments': 1, 'Shares': 1}, 
#     {'Likes': 19, 'Comments': 3}
# ]
# total_likes = 0

# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError as error_message:
#         print(f'{error_message} does not exist in the dictionary')
#         total_likes += 0

# print(total_likes)


# #Exercise 3: Catch exceptions in the code
# import pandas

# data = pandas.read_csv('../Data/nato_phonetic_alphabet_26.csv')
# nato_alphabet_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# # is_on = True

# # while is_on:
# #     user_input = input('Enter a word: ').upper()
# #     try:
# #         code_list = [nato_alphabet_dict[letter] for letter in user_input]
# #     except KeyError:
# #         print('sorry, only letter in the alphabet please')
# #     else:
# #         is_on = False
# #         print(code_list)

# def pass_gen():
#     user_input = input('Enter a word: ').upper()
#     try:
#         code_list = [nato_alphabet_dict[letter] for letter in user_input]
#     except KeyError:
#         print('sorry, only letter in the alphabet please')
#         pass_gen()
#     else:
#         is_on = False
#         print(code_list)

# pass_gen()


# project - Edit password manager project to save to a json
from tkinter import * 
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def press():
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])

    shuffle(password_list)

    password_text = ''.join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password_text)
    
    pyperclip.copy(password_text)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title='Oops', message='You have an empty field!')
    else: 
        data = {
                website: {
                    'email': email,
                    'password': password,
                }
            }
        try:
            with open('../Data/data_30.json', 'r') as f:
                new_data = json.load(f)
        except FileNotFoundError:
            with open('../Data/data_30.json', 'w') as f:
                json.dump(data, f, indent=4)
        else:
            new_data.update(data)
            with open('../Data/data_30.json', 'w') as f:
                json.dump(new_data, f, indent=4)
        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- LOAD PASSWORD ------------------------------- #
def search():
    website = website_input.get()
    try:
        with open('../Data/data_30.json', 'r') as f:
            data_file = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo('Error!', 'No data file found.')
    else:
        if website in data_file:
            saved_email = data_file[website]['email']
            saved_password = data_file[website]['password']
            messagebox.showinfo(website, 
                                f'Email: {saved_email}\nPassword: {saved_password}')
        else:
            messagebox.showinfo('Error!', f'No details for {website} exists')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file='../Data/logo_29.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
email_label.config(padx=10)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

website_input = Entry()
website_input.grid(column=1, row=1, sticky='EW')
website_input.focus()

email_input = Entry()
email_input.grid(column=1, row=2, columnspan=2, sticky='EW')

password_input = Entry()
password_input.grid(column=1, row=3, sticky='EW')

generate_button = Button(text='Generate Password', width=15, command=press)
generate_button.grid(column=2, row=3, sticky='E')

add_button = Button(text='Add', width=45, command=save_info)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', width=15, command=search)
search_button.grid(column=2, row=1, sticky='E')


window.mainloop()