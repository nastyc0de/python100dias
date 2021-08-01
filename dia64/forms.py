from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

class ReviewForm(FlaskForm):
    rating = IntegerField('New rating', validators=[DataRequired()])
    review = StringField('New review', validators=[DataRequired()])
    done = SubmitField('Done')

class AddForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    add = SubmitField('Add movie')