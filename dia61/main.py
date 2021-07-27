from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class Form(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(message='Este campo es obligatorio'), Email(message='Debes de agregar un @')])
    password = PasswordField(label='Password', validators=[DataRequired(message='Este campo es obligatorio'), Length(8,message='Debes de agregar al menos 8 caracteres')])
    submit = SubmitField(label='Log In')
    
app = Flask(__name__)
app.secret_key = "some secret string"


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = Form()
    form.validate_on_submit()
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)