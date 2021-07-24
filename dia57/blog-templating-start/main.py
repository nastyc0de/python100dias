from flask import Flask, render_template
from post import Post
from api import data
postList = []
for post in data:
    postItem = Post(post['id'],post['title'], post['body'])
    postList.append(postItem)

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html", posts=postList)

@app.route('/post/<int:id>')
def post(id):
    for postInfo in postList:
        if postInfo.id == id:
            info = postInfo
    return render_template("post.html", post=info)

if __name__ == "__main__":
    app.run(debug=True)