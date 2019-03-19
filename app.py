from flask import Flask, g
from flask import render_template, flash, redirect, url_for, request

import models
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
def hello_world():
  if request.method == 'GET':
    return 'Hello, World!'
  elif request.method == 'POST':
    return

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


