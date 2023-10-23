from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_words = {}

###### GENERATE WORDS ######
try:
    data = pandas.read_csv('../Data/31/words_to_learn_31.csv')
except FileNotFoundError:
    data = pandas.read_csv('../Data/31/french_words_31.csv')
finally:
    all_words = data.to_dict(orient='records')

###### CARD FLIP ######
def green_card():
    canvas.itemconfig(canvas_image, image=green_image)
    canvas.itemconfig(word_text, fill='white', text=random_words['English'])
    canvas.itemconfig(title_text, fill='white', text='English')
    
def pick_word():
    global random_words, timer
    window.after_cancel(timer)
    random_words = random.choice(all_words)
    canvas.itemconfig(canvas_image, image=white_image)
    canvas.itemconfig(word_text, fill='black', text=random_words['French'])
    canvas.itemconfig(title_text, fill='black', text='French')
    timer = window.after(3000, green_card)

###### BUTTON ACTION ######
def green_button():
    all_words.remove(random_words)
    new_data = pandas.DataFrame(all_words)
    new_data.to_csv('../Data/31/words_to_learn_31.csv', index=False)
    pick_word()

###### UI ######
window = Tk()
window.title('Flash Cards')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

timer = window.after(3000, green_card)

green_image = PhotoImage(file='../Data/31/card_back_31.png')
white_image = PhotoImage(file='../Data/31/card_front_31.png')
canvas = Canvas(width=800, height=536, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=white_image)
title_text = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file='../Data/31/wrong_31.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=pick_word)
wrong_button.grid(column=0, row=1)
wrong_button.config(pady=50)

right_image = PhotoImage(file='../Data/31/right_31.png')
right_button = Button(image=right_image, highlightthickness=0, command=green_button)
right_button.grid(column=1, row=1)
right_button.config(pady=50)

pick_word()

window.mainloop()