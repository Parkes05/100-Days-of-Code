# # Exercise 1
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1, 2, 3, 4, 5, 6, 7, 8))

def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    return n

print(calculate(2, add=2, multiply=4))


# # Exercise 2
from tkinter import *

window = Tk()
window.title('My first GUI program')
window.minsize(height=500, width=500)

# labels
m_label = Label(text='I am a label', font=('Ariel', 24, 'bold'))
m_label.pack()

def on_click():
    global m_label
    m_label.config(text=input.get())
    # m_label['text'] = 'Button Got Clicked'

# button
button = Button(text='Click me', command=on_click)
button.pack()

# entry
input = Entry(width=30)
input.insert(END, string='@email')
input.pack()
print(input.get())

# text
text = Text(width=30, height=5)
text.focus()
text.insert(END, 'How are you doing\nI am fine')
text.pack()
print(text.get('1.0', END))

def print_spinbox():
    print(spinbox.get())

# spinbox
spinbox = Spinbox(width=5, from_=0, to=10, command=print_spinbox)
spinbox.pack()

def print_scale(value):
    print(value)

# scale
scale = Scale(from_=0, to=100, command=print_scale)
scale.pack()

def print_check():
    # 1 for on and 0 for off
    print(checked_state.get())

#checkbutton
checked_state = IntVar()
check_button = Checkbutton(text='Is On', variable=checked_state, command=print_check)
check_button.pack()

def print_radio():
    print(radio_state.get())

# Radiobutton
radio_state = IntVar()
radio_button_1 = Radiobutton(text='Option 1', value=1, variable=radio_state, command=print_radio)
radio_button_2 = Radiobutton(text='Option 2', value=2, variable=radio_state, command=print_radio)
radio_button_1.pack()
radio_button_2.pack()

def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

fruits = ["Apple", "Pear", "Orange", "Banana"]
listbox = Listbox(height=len(fruits))
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


# Project
from tkinter import *

def when_clicked():
    number = float(input.get())
    result = round(number * 1.609344, 2)
    label_2.config(text=f'{result}')

window = Tk()
window.title('Miles to kilometer converter')
window.config(padx=20, pady=20)

label_1 = Label(text='is equal to', font=('Ariel', 12))
label_1.grid(column=0, row=1)
label_1.config(padx=10)

label_2 = Label(text='0', font=('Ariel', 12))
label_2.grid(column=1, row=1)

label_3 = Label(text='Km', font=('Ariel', 12))
label_3.grid(column=2, row=1)
label_3.config(padx=10)

label_4 = Label(text='Miles', font=('Ariel', 12))
label_4.grid(column=2, row=0)
label_4.config(padx=10)

button = Button(text='Calculate', command=when_clicked)
button.grid(column=1, row=2)

input = Entry(width=10)
input.grid(column=1, row=0)



window.mainloop()