from turtle import Turtle
ALIGNMENT = 'center'
FRONT = ('Courier', 16, 'bold')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.setposition(x=0, y=270)
        self.write_score()
    
    def write_score(self):
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FRONT)
    
    def increase_score(self):
        self.score += 1
        self.write_score()
    
    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.write_score()
    
    # def game_over(self):
    #     self.setposition(x=0, y=0)
    #     self.write(arg='GAME OVER', align=ALIGNMENT, font=FRONT)
