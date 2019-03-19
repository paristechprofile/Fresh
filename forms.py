# import the tools and fields we need
from flask_wtf import FlaskForm as Form
from wtforms import TextField, TextAreaField, SubmitField

# import the Review model
from models import Review

# create the class and variables to house Field definitions
class ReviewForm(Form):
  barber = TextField('By:')
  user = TextField('Title')
  text = TextAreaField('Review')
  rating = TextField('Rating')
  submit = SubmitField('Create Review')
