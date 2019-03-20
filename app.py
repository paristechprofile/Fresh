from flask import Flask, g
from flask import render_template, flash, redirect, url_for, request
import json
import models
from forms import ReviewForm
# from forms import ReviewForm 
# create the above form

DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = 'adkjfalj.adflja.dfnasdf.asd'

@app.before_request
def before_request():
  g.db = models.DATABASE
  g.db.connect()

@app.after_request
def after_request(res):
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

if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)

# @app.route('/review', methods=['POST'])
# @app.route('/review/<reviewid>', methods=['GET'])
# def get_create_review(reviewid=None):
#     from models import Review
#     if reviewid == None:
#         user = request.json['user']
#         title = request.json['title']
#         text = request.json['text']
#         sub = request.json['sub']

#         return Comments.create_comment(user, title, text, sub)
#     else:
#         return Comments.get_comment(commentid)

# # @app.route('/comments')
# # def hello_world():
# #   return 'Hello World'


