from logging import debug
import re
from flask import Flask
app = Flask(__name__)

print(__name__)
@app.route('/')
def hello():
    return 'Hello World'
@app.route('/bye')
def bye():
    return 'Bye'
@app.route('/username/<name>')
def user(name):
    return f'Hello, {name}'

if __name__ == "__main__":
    app.run(debug=True)