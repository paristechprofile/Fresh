from flask import Flask, g
from flask import render_template, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import check_password_hash
import json
import models
import forms
from forms import ReviewForm
from forms import EditForm
from flask_bootstrap import Bootstrap
import os

if 'ON_HEROKU' in os.environ:
  print('hitting ')
  models.initialize()

DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = '!ohy.ouf.ancyh.uh?'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.before_request
def before_request():
  
  g.db.connect()


@login_manager.user_loader
def load_user(userid):
  try:
    return models.User.get(models.User.id == userid)
  except models.DoesNotExist:
    return None

@app.before_request
def before_request():
  """Connect to the database before each request."""
  g.db = db_proxy #https://swifthorseman.com/2015/06/18/deploying-a-flask-app-with-peewee-to-heroku/
  # g.db = models.DATABASE #peewee
  g.db.connect()
  g.user = current_user

@app.after_request
def after_request(res):
  """Close the database connection after each request."""
  g.db.close()
  return res

@app.route('/')
def index():
  stream = models.Post.select().limit(100)
  return render_template('home.html', stream=stream)

@app.route('/stream')
@app.route('/stream/<username>')
@login_required

def stream(username=None):
  template = 'stream.html'
  if username and username != current_user.username:
    user = models.User.select().where(models.User.username == username).get()
    stream = user.posts.limit(100)
  else:
    stream = current_user.get_stream().limit(100)
    user = current_user
  if username:
    template = 'user_profile.html'
  return render_template(template, stream=stream, user=user)


@app.route('/register', methods=('GET', 'POST'))
def register():
  form = forms.RegisterForm()
  if form.validate_on_submit():
    flash('You in bruh. Damn straight!', 'success')
    models.User.create_user(
      username=form.username.data,
      email=form.email.data,
      password=form.password.data
      )
    return redirect(url_for('index'))
  return render_template('register.html', form=form)

@app.route('/login', methods=('GET', 'POST'))
def login():
  form = forms.LoginForm()
  if form.validate_on_submit():
    try:
      user = models.User.get(models.User.email == form.email.data)
    except models.DoesNotExist:
      flash("your email or password doesn't match", "error")
    else:
      if check_password_hash(user.password, form.password.data):
        login_user(user)
        flash("You've been logged in", "success")
        return redirect(url_for('index'))
      else:
        flash("your email or password doesn't match", "error")
  return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
  logout_user()
  flash("You've been logged out", "success")
  return redirect(url_for('index'))

@app.route('/new_post', methods=('GET', 'POST'))
@login_required
def post():
  form = forms.PostForm()
  if form.validate_on_submit():
    models.Post.create(user=g.user._get_current_object(), content=form.content.data.strip())
    flash("Message posted! Thanks!", "success")
    return redirect(url_for('index'))
  return render_template('posts.html', form=form)

@app.route('/barbers')
@app.route('/barbers/<id>', methods=['GET', 'POST'])
def barbers(id=None):
  if id == None:
    barbers = models.Barber.select().limit(100)
    return render_template('barbers.html', barbers=barbers)
  else:
    barber_param = int(id)
    barber = models.Barber.get(models.Barber.id == barber_param)
    reviews = barber.reviews
    form = ReviewForm()
    if form.validate_on_submit():
      models.Review.create(
        barber=barber_param, 
        user_id=g.user._get_current_object(),
        text=form.text.data.strip(), 
        rating=form.rating.data.strip()
        )
      flash("You created a review")
    return render_template("barber.html", barber=barber, reviews=reviews,form=form)

@app.route('/barbers/<barberid>/reviews/<id>/delete')
def delete_review(barberid, id):
  review_param = int(id)
  barber_param = int(barberid)
  review = models.Review.get_or_none(review_param)
  if str(review.user_id) == str(current_user.id):
    review.delete_instance()
    form = ReviewForm()
    barber = models.Barber.get(models.Barber.id == barber_param)
    reviews = barber.reviews
    flash('you deleted your review')
    return redirect(url_for('barbers', id=barber_param))
  else:
    flash('you cannot delete a review that is not yours')
  return redirect(url_for('barbers', id=barber_param))

@app.route('/barbers/<barberid>/reviews/<id>/edit', methods=('GET', 'POST'))
def edit_review(barberid, id):
  review_param = int(id)
  barber_param = int(barberid)
  review = models.Review.get(models.Review.id == review_param)
  form = EditForm()
  barber = models.Barber.get(models.Barber.id == barber_param)
  if form.validate_on_submit():
    review.text = form.text.data
    review.rating = form.rating.data
    review.save()
    flash('you edited your review')
    return redirect(url_for('barbers', id=barber_param))
  else: 
    flash('make sure to fill out both fields and that your review is 0-5')
    return render_template("edit_form.html", id=barber_param, review=review, form=form)

if __name__ == '__main__':
  models.initialize()
  try:
    models.User.create_user(
      username='paris',
      email='fake@gmail.com',
      password='whynot',
      admin=True
      )
  except ValueError:
    pass
  app.run(debug=DEBUG, port=PORT)