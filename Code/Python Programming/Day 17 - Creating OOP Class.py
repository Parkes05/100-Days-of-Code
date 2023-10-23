import sys
sys.path.append('../Data')
from question_model_17 import Question
from data_17 import question_data
from quiz_brain_17 import QuizBrain
import os

os.system('cls')

question_bank = []
for questions in question_data:
    question_text = questions['text']
    question_answer = questions['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print('Your have completed the quiz')
print(f'Your final score was: {quiz.score}/{quiz.question_number}')

    