from flask import Flask, g, request
from flask import render_template, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import check_password_hash
import json
import models
<<<<<<< HEAD

=======
import forms
>>>>>>> 3af8c0b7b85c2d2cc30ed515b1b7c1ff0fd5942b
from forms import ReviewForm
from forms import EditForm
from flask_bootstrap import Bootstrap

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
  g.user = current_user

@app.after_request
def after_request(res):
  """Close the database connection after each request."""
  g.db.close()
  return res

@app.route('/')
def index():
<<<<<<< HEAD
  return render_template('hello.html')



@app.route('/reviews', methods=['GET', 'POST'])
def review():
    # the form variable we send down to the template needs to be added here
  form = ReviewForm()
  return render_template("new_review.html", title="New Review", form=form)



# ##########################################################
# #################### Delete A Post ###################
# ##########################################################

@app.route('/review/<id>/put', methods=['POST'])
def delete_review(id=None):
  form = ReviewForm()
 
  review_id = int(id)

  review = models.Review.get(models.Review.id == review_id)

  review.delete_instance()
  
  reviews = models.Review.select().limit(100)

  
  return render_template("new_review.html", reviews=reviews, form=form) 


# ##########################################################
# #################### Delete A Post ###################
# ##########################################################












# ##########################################################
# #################### Going into edit Mode ###################
# ##########################################################

@app.route('/review/<id>/edit_mode', methods=['POST'])
def edit_mode(id=None):
  form = ReviewForm()

  reviews = models.Review.select().limit(100)
  
  return render_template("edit_template.html", reviews=reviews, form=form)


# ##########################################################
# #################### Going into Edit Mode ###################
# ##########################################################



























# ##########################################################
# #################### Updating A Post ###################
# ##########################################################

@app.route('/review/<id>/update', methods=['POST'])
def update_review(id=None):
  form = ReviewForm()
  Review = models.Review

  review_id = int(id)
  
  print(form.text, 'gfgfgfgfgfgfgfgf')
  print(form.text, 'gfgfgfgfgfgfgfgf')
  print(form.text, 'gfgfgfgfgfgfgfgf')
  print(form.text, 'gfgfgfgfgfgfgfgf')

  query = Review.update(text='chike').where(Review.id == review_id)

  query.execute()

  reviews = Review.select().limit(100)

  return render_template("new_review.html", reviews=reviews, form=form) 


# ##########################################################
# #################### Updating A Post ###################
# ##########################################################





# ##########################################################
# #################### Setting Up A Post ###################
# ##########################################################

@app.route('/reviews/', methods=['GET', 'POST'])
@app.route('/reviews/', methods=['GET'])
def reviews():
  form = ReviewForm()
  # if request.method == 'GET' and delete != None:
  #   return redirect('new_review.html')
  # if request.args.get('id') == 'chike':
  #   print('hello , hello , hello')
  #   return 'hello'

  print(request.args.get('id'))

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
    # return render_template('new_review.html', title="New Review", form=form)

#################################################################
#################### End of Setting Up A Post ###################
#################################################################




@app.route('/barbers', methods=['GET', 'POST'])
def barbers():
  with open('barbers.json') as json_data:
    barbers = json.load(json_data)
    return render_template('barbers.html', barbers=barbers)
=======
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
>>>>>>> 3af8c0b7b85c2d2cc30ed515b1b7c1ff0fd5942b

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