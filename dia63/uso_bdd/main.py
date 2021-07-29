from datetime import time
import sqlite3
from sqlite3.dbapi2 import connect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

createdb = sqlite3.connect('new-books-collection.db')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# . INTEGER/FLOAT/VARCHAR/UNIQUE/NOT NULL 
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True,nullable=False)
    author = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __str__(self) -> str:
        return f'Book: {self.title}'
db.create_all()
# crear un nuevo registro
new_book = Book(id=1, title='LOTR', author='Tolkien', rating=9.1)
db.session.add(new_book)
db.session.commit()
# db = sqlite3.connect('booksDB.db')
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# # cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# cursor.execute("INSERT INTO books VALUE(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
