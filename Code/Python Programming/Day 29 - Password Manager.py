from tkinter import * 
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

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
        is_ok = messagebox.askokcancel(title='Confirm', message=f'You have entered\n\nWebsite: {website}\n'
                                       f'Email/Username: {email}\nPassword: {password}\n\nIs this okay?')
        if is_ok:
            sentence = f'Website: {website}\nEmail/Username: {email}\nPassword: {password}\n\n'
            
            with open('dete.txt', mode='a') as f:
                f.write(sentence)

            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()
            email_input.insert(END, f'{email}')

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
website_input.grid(column=1, row=1, columnspan=2, sticky='EW')
website_input.focus()

email_input = Entry()
email_input.grid(column=1, row=2, columnspan=2, sticky='EW')

password_input = Entry()
password_input.grid(column=1, row=3, sticky='EW')

generate_button = Button(text='Generate Password', command=press)
generate_button.grid(column=2, row=3, sticky='E')

add_button = Button(text='Add', width=45, command=save_info)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()