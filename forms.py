# import the tools and fields we need
from flask_wtf import FlaskForm as Form
from wtforms import TextField, TextAreaField, StringField, PasswordField, SubmitField, SelectField
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
  barber = StringField('Barber:')
  user = StringField('User:')
  text = TextAreaField('Review')
  rating = StringField('Rating')
  submit = SubmitField('Create Review')

class EditForm(Form):
  barber = StringField('Barber:')
  user = StringField('User:')
  text = TextAreaField('Review', validators=[DataRequired()])
  rating = StringField('Rating', validators=[
    DataRequired(),
    Regexp(
      r'^[0-5_]+$',
      message=("Rating should be 0-5 only")
    )
  ])
  submit = SubmitField('Save')


class PostForm(Form):
  content = TextAreaField("Enter Post here", validators=[DataRequired()])
<<<<<<< HEAD
=======
  neighborhood = SelectField(u'Choose Neighborhood', choices=[('soma', 'SOMA'), 
                                                              ('dp', 'DOGPATCH'), 
                                                              ('md', 'MISSION DISTRICT'), 
                                                              ('ga', 'GENERAL ASSEMBLY')])
  search = SubmitField('Search')
>>>>>>> chike_branch
