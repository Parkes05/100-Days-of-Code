from flask import Flask

def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper

def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper

app = Flask(__name__)

@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello():
    return 'Hello!'

@app.route('/<name>/<int:number>')
def greet(name, number):
    return f'Hello there {name}{number}!'


if __name__ == '__main__':
    app.run(debug=True)



###### Exercise ######
inputs = eval(input())
# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f'You called {function.__name__}{args}')
        result = function(args[0], args[1], args[2])
        print(f'It returned: {result}')
    return wrapper

# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(inputs[0], inputs[1], inputs[2])



from flask import Flask
import random


def heading(function):
    def wrapper():
        return f'<h1>{function()}</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="numbers from 0 to 9"/>'
    return wrapper

def body(function):
    def wrapper(number):
        result = function(number)
        if result == 'right':
            return '<h1 style="color: green">You found me!</h1><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="Dog poking out of a container" style="width: 200px" />'
        elif result == 'low':
            return '<h1 style="color: red">Too low, try again!</h1><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="Dog resting at the foot of a tree" style="width: 200px" />'
        else:
            return '<h1 style="color: purple">Too high, try again!</h1><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="Human hand holding a dog" style="width: 200px" />'
    return wrapper

num = random.randint(0, 9)

app = Flask(__name__)

@app.route('/', endpoint='home_screen')
@heading
def home_screen():
    return 'Guess a number between 0 and 9'

@app.route('/<int:number>', endpoint='game')
@body
def game(number):
    if number == num:
        return 'right'
    elif number > num:
        return 'high'
    else:
        return 'low'

if __name__ == '__main__':
    app.run(debug=True)