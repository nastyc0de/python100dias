from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True,nullable=False)
    author = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __str__(self) -> str:
        return f'Book: {self.title}'

db.create_all()
@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method =='POST':
        # new_book = Book(id=1, title='LOTR', author='Tolkien', rating=9.1)
        new_book = Book(
            title= request.form['title'],
            author= request.form['author'],
            rating = request.form['rating']
        )
        db.session.add(new_book)
        db.session.commit()
        
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    book = Book.query.get_or_404(id)
    if request.method == "POST":
        new_rating = request.form['rating']
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', book=book)
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))
if __name__ == "__main__":
    app.run(debug=True)

