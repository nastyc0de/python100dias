from logging import debug
from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    date = datetime.datetime.now().strftime("%Y")
    rand_num = random.randint(1, 10)
    return render_template('index.html',num=rand_num, year=date)
if __name__ == "__main__":
    app.run(debug=True)
    