# import the tools and fields we need
from flask_wtf import FlaskForm as Form
from wtforms import TextField, TextAreaField, StringField, PasswordField, SubmitField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email, Length, EqualTo)
from models import Review
from models import User

def username_exists(form, field):
  if User.select().where(User.username == field.data).exists():
    raise ValidationError('User with that username already exists.')


def email_exists(form, field):
  if User.select().where(User.email == field.data).exists():
    raise ValidationError('User with that email already exists.')

class RegisterForm(Form):
  username = StringField(
    'Username',
    validators=[
        DataRequired(),
        Regexp(
          r'^[a-zA-Z0-9_]+$',
          message=("Username should be one word, letters, numbers, and underscores only.")
        ),
        username_exists
    ])
  email = StringField(
    'Email',
    validators=[
      DataRequired(),
      Email(),
      email_exists
    ])
  password = PasswordField(
    'Password',
    validators=[
      DataRequired(),
      Length(min=2),
      EqualTo('password2', message='Passwords must match')
    ])
  password2 = PasswordField(
    'Confirm Password',
    validators=[DataRequired()]
    )

class LoginForm(Form):
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])

# create the class and variables to house Field definitions
class ReviewForm(Form):
  barber = TextField('By:')
  user = TextField('Title')
  text = TextAreaField('Review')
  rating = TextField('Rating')
  submit = SubmitField('Create Review')