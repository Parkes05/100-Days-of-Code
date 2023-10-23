class QuizBrain:

    def __init__(self, questionlist):
        self.quesion_list = questionlist
        self.question_number = 0
        self.score = 0
    
    def still_has_questions(self):
        return self.question_number < len(self.quesion_list)
    
    def next_question(self):
        q_text = self.quesion_list[self.question_number]
        self.question_number += 1
        answer = input(f'Q.{self.question_number}: {q_text.text} (True/False)?: ')
        self.check_answer(answer, q_text.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right')
            self.score += 1
        else:
            print('That\'s wrong.')
        print(f'The correct answer was: {correct_answer}')
        print(f'Your current score is: {self.score}/{self.question_number}\n')
