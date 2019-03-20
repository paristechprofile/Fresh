from flask import Flask, g
from flask import render_template, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import check_password_hash
import json
import models
from forms import ReviewForm
# from forms import ReviewForm 
# create the above form

DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = '!ohy.ouf.ancyh.uh?'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
  try:
    return models.User.get(models.User.id == userid)
  except models.DoesNotExist:
    return None

@app.before_request
def before_request():
  """Connect to the database before each request."""
  g.db = models.DATABASE
  g.db.connect()

@app.after_request
def after_request(res):
  """Close the database connection after each request."""
  g.db.close()
  return res

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('hello.html')



# @app.route('/reviews', methods=['GET', 'POST'])
# def review():
#     # the form variable we send down to the template needs to be added here
#   form = ReviewForm()
#   return render_template("new_review.html", title="New Review", form=form)


##########################################################
#################### Setting Up A Post ###################
##########################################################
@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
  form = ReviewForm()
  if request.method == 'GET':
    reviews = models.Review.select().limit(100)
    return render_template("new_review.html", reviews=reviews, form=form)
  else:
      # checks if the form submission is valid
    if form.validate_on_submit():
          # if it is, we create a new Sub
      models.Review.create(
        barber=form.barber.data.strip(), 
        user=form.user.data.strip(), 
        text=form.text.data.strip(), 
        rating=form.rating.data.strip()
        )
      reviews = models.Review.select().limit(100)
      flash("New review registered. Called: {}".format(form.barber.data))
          # and redirect to the main Sub index
      return render_template("new_review.html", reviews=reviews, form=form)
    # if the submission isn't valid, send the user back to the original view
    return render_template('new_review.html', title="New Review", form=form)

#################################################################
#################### End of Setting Up A Post ###################
#################################################################












# @app.route('/barbers', methods=['GET', 'POST'])
# def barbers():
#   with open('barbers.json') as json_data:
#     barbers = json.load(json_data)
#     return render_template('barbers.html', barbers=barbers)

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