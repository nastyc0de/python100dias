from flask import Flask, render_template
from api import posts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

# contact
@app.route('/contact')
def contact():
    return render_template('contact.html')
# about
@app.route('/about')
def about():
    return render_template('about.html')
# posts
@app.route('/post/<int:id>')
def post(id):
    req_post = None
    for post in posts:
        if post['id'] == id:
            req_post = post
    return render_template('post.html', req_post = req_post)
        

if __name__ =='__main__':
    app.run(debug=True)