from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/post/<id>')
def post(id):
    print(id)
if __name__ == "__main__":
    app.run(debug=True)
