from logging import debug
from flask import Flask
import random

random_number = random.randint(0,9)
print(random_number)

app = Flask(__name__)

def decarator_title(function):
    def internal_function():
        return f"<h1 style='text-align: center'>{function()}</h1>"
    return internal_function

@app.route('/')
@decarator_title
def home():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1> \
        <div style="text-align: center"><iframe src="https://giphy.com/embed/l378khQxt68syiWJy" width="480" height="480" frameBorder="0"></iframe></div>'

@app.route("/<int:number>")
def page(number):
    if number > random_number:
        return '<h1 style="text-align: center">To high try with a lower number</h1> \
        <div style="text-align: center"><iframe src="https://giphy.com/embed/l2JhAWfg8r8OlIvhS" width="480" height="480" frameBorder="0"></iframe></div>'
    elif number < random_number:
        return '<h1 style="text-align: center">To lower try a high number</h1> \
        <div style="text-align: center"><iframe src="https://giphy.com/embed/l2JhAWfg8r8OlIvhS" width="480" height="480" frameBorder="0"></iframe></div>'
    else:
        return '<h1 style="text-align: center">Correct you found the page</h1> \
        <div style="text-align: center"><iframe src="https://giphy.com/embed/26tknCqiJrBQG6bxC" width="480" height="480" frameBorder="0"></iframe></div>'

if __name__ == '__main__':
    app.run(debug=True)