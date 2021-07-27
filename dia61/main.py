from form import MyForm
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'my_secret'

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    form.validate_on_submit()
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)