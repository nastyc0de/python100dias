from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    res = requests.get(url='https://jsonplaceholder.typicode.com/posts')
    data = res.json()
    return render_template("index.html", posts=data)
@app.route('/post/<int:id>')
def post(id):
    res = requests.get(url='https://jsonplaceholder.typicode.com/posts')
    data = res.json()
    info = data[id-1]
    return render_template("post.html", post=info)
if __name__ == "__main__":
    app.run(debug=True)
