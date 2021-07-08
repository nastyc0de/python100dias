from logging import debug
from flask import Flask, render_template
import random
import datetime
import requests



app = Flask(__name__)

@app.route('/')
def home():
    date = datetime.datetime.now().strftime("%Y")
    rand_num = random.randint(1, 10)
    return render_template('index.html',num=rand_num, year=date)

@app.route('/guess/<name>')
def guess(name):
    parameters = {
    'name': name
    }
    response = requests.get(url='https://api.agify.io', params=parameters )
    response_genre = requests.get(url='https://api.genderize.io', params=parameters)
    data_genre = response_genre.json()
    data = response.json()
    return render_template('name.html', name=data['name'].title(), age=data['age'], genre= data_genre['gender'])
@app.route('/blog/<num>')
def blog(num):
    print(num)
    response = requests.get(url='https://jsonplaceholder.typicode.com/posts')
    posts = response.json()
    return render_template('blog.html', posts=posts)
if __name__ == "__main__":
    app.run(debug=True)
    