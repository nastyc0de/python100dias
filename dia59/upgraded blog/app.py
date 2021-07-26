from flask import Flask, render_template, request
from api import posts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

# contact
@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        print(f'{name},{email},{phone},{message}')
        # msg = 'Datos enviado correctamente'
    return render_template('contact.html')
# getting data
# @app.route('/getData', methods=['POST', 'GET'])
# def getData():

#     name = request.form['name']
#     email = request.form['email']
#     phone = request.form['phone']
#     message = request.form['message']
#     print(f'{name},{email},{phone},{message}')
#     return 'Datos enviados'
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