## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

##Functions can be nested in other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()

## Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function()
inner_function


## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")

decorated_function = delay_decorator(say_greeting)
decorated_function()

say_hello()
say_bye()



## Exercise
import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970

def speed_calc_decorator(function):
  def warper_function():
    start = time.time()
    function()
    end = time.time()
    print(f'{function.__name__} run speed: {end - start}s')
  return warper_function

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i

@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()
slow_function()



## Flask start
from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route('/bye')
def bye():
    return 'Bye'

if __name__ == '__main__':
    app.run()