from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def internal():
        return f'<b>{function()}</b>'
    return internal
def make_underline(function):
    def internal():
        return f'<u>{function()}</u>'
    return internal
def make_emphasis(function):
    def internal():
        return f'<em>{function()}</em>'
    return internal


@app.route('/')
@make_bold
@make_underline
@make_emphasis
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