import requests, html
from tkinter import *

THEME_COLOR = '#375362'

class Quizzler:

    def __init__(self):
        self.questions = []
        self.number = 0
        self.score = 0
        self.create_question()

    def create_question(self, number_of_questions=10):
        trivia_url = 'https://opentdb.com/api.php?amount=10&type=boolean'
        parameters = {
            'amount': number_of_questions,
            'type': 'boolean',
        }

        response = requests.get(url=trivia_url, params=parameters)
        response.raise_for_status()
        data = response.json()
        self.questions = data['results']
    
    def next_question(self):
        current_question = self.questions[self.number]['question']
        question_text = html.unescape(current_question)
        self.current_answer = self.questions[self.number]['correct_answer']
        self.number += 1
        return f'Q.{self.number}: {question_text}'

    def check_answer(self, input: str):
        if input == self.current_answer:
            self.score += 1
            return True
        else:
            return False
    
    def still_has_questions(self):
        return self.number < len(self.questions)


class QuizGui(Quizzler):

    def __init__(self, quiz_brain: Quizzler):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler Game')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.text = self.canvas.create_text(150, 125, 
                                font=('Arial', 20, 'italic'), text='', 
                                width=280, fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        good_image = PhotoImage(file='../Data/34/true_34.png')
        self.good_button = Button(highlightthickness=0, image=good_image, command=self.check_right)
        self.good_button.grid(column=0, row=2)

        bad_image = PhotoImage(file='../Data/34/false_34.png')
        self.bad_button = Button(highlightthickness=0, image=bad_image, command=self.check_wrong)
        self.bad_button.grid(column=1, row=2)

        self.label = Label(bg=THEME_COLOR, fg='white', text=f'Score: 0', font=('Arial', 15, 'bold'))
        self.label.grid(column=1, row=0)

        self.get_next_question()


        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text='You\'ve reached the end of the Quiz')
            self.good_button.config(state='disabled')
            self.bad_button.config(state='disabled')
    
    def check_right(self):
        self.do_something('True')
    
    def check_wrong(self):
        self.do_something('False')

    def do_something(self, answer: str):
        ans = self.quiz.check_answer(answer)
        if ans:
            self.label.config(text=f'Score: {self.quiz.score}')
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)