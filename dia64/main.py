from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from api import call_movie
from forms import ReviewForm, AddForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(15))
    description = db.Column(db.String(200))
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(100))
    img_url = db.Column(db.String(20))
    
    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Movie {self.title}>'
    
@app.route("/")
def home():
    all_movie =Movie.query.all()
    return render_template("index.html", movies=all_movie)

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    movie = Movie.query.get_or_404(id)
    movieForm = ReviewForm(obj=movie)
    if request.method == 'POST':
        if movieForm.validate_on_submit():
            movieForm.populate_obj(movie)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('edit.html', form=movieForm, movie=movie)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))
@app.route('/add', methods=['GET', 'POST'])
def add():
    movie = Movie.title
    addForm = AddForm(obj=movie)
    if request.method == 'POST':
        if addForm.validate_on_submit():
            title = request.form['title']
            new_movie = call_movie(title)
            add_movie = Movie(
                title=new_movie['title'],
                year= new_movie['year'],
                description=new_movie['description'],
                rating=0,
                ranking=0,
                review='Insert something',
                img_url=new_movie['img']
            )
            print(add_movie.id)
            db.session.add(add_movie)
            db.session.commit()
            return redirect('/')
    return render_template('add.html', form=addForm)
if __name__ == '__main__':
    app.run(debug=True)
