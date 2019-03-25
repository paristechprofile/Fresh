# import datetime
# import os
# from peewee import *
# from flask_login import UserMixin
# from flask_bcrypt import generate_password_hash
# from playhouse.db_url import connect
# from flask import g

# # DATABASE_URL = os.environ['DATABASE_URL'] #heroku directions https://devcenter.heroku.com/articles/heroku-postgresql
# # conn = psycopg2.connect(DATABASE_URL, sslmode='require') #heroku directions https://devcenter.heroku.com/articles/heroku-postgresql

# # DATABASE = SqliteDatabase('fresh.db') #sqlite database
# DATABASE = connect(os.environ.get('DATABASE_URL')) #for heroku database

# class User(UserMixin, Model):
#   username = CharField(unique=True)
#   email = CharField(unique=True)
#   password  = CharField(max_length=100)
#   joined_at = DateTimeField(default=datetime.datetime.now)
#   is_admin = BooleanField(default=False)

#   class Meta:
#     database = DATABASE
  
#   def get_posts(self):
#     return Post.select().where(Post.user == self)

#   def get_stream(self):
#     return Post.select().where(
#       (Post.user == self)
#     )
    
#   @classmethod
#   def create_user(cls, username, email, password, admin=False):
#     try:
#       cls.create(
#         username=username,
#         email=email,
#         password=generate_password_hash(password),
#         is_admin=admin
#       )
#     except IntegrityError:
#       raise ValueError("User already exists")

# class Barber(Model):
#   name = CharField()
#   neighborhood = CharField()
#   profile_pic = CharField()
#   portfolio_pic = CharField()

#   class Meta:
#     database = DATABASE

# #############################################################
# #################### Review Model Methods ###################
# #############################################################

# class Review(Model):
#   timestamp = DateTimeField(default=datetime.datetime.now)
#   barber = ForeignKeyField(Barber, backref='reviews')
#   user_id = ForeignKeyField(User, backref='reviews')
#   text = TextField()
#   rating = CharField()

#   class Meta:
#     database = DATABASE
#     order_by = ('-timestamp',)

# class Post(Model):
#   timestamp = DateTimeField(default=datetime.datetime.now)
#   user = ForeignKeyField(
#     model=User,
#     backref='posts'
#   )
#   content = TextField()

#   class Meta:
#     database = DATABASE
#     order_by = ('-timestamp',)

# def initialize():
#   DATABASE.connect()
#   DATABASE.create_tables([User, Barber, Review, Post], safe=True)
#   DATABASE.close()



#
#
#



import datetime
import os
from peewee import *
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash
# from playhouse.postgres_ext import PostgresqlExtDatabase
from playhouse.db_url import connect
from flask import g
# import psycopg2

# DATABASE = PostgresqlDatabase('fresh')

DATABASE = connect(os.environ.get('DATABASE_URL'))

# DATABASE_URL = os.environ['DATABASE_URL'] #heroku directions https://devcenter.heroku.com/articles/heroku-postgresql
# conn = psycopg2.connect(DATABASE_URL, sslmode='require') #heroku directions https://devcenter.heroku.com/articles/heroku-postgresql

# DATABASE = connect(os.environ.get('DATABASE_URL')) #for heroku database
# DATABASE = SqliteDatabase('fresh.db') #sqlite database

# pg_db = PostgresqlDatabase('fresh', user='paristaylor', password='secret',
#                            host='10.1.0.9', port=5432)


# if 'HEROKU' in os.environ:
#   psql_db = PostgresqlDatabase('d75hp2sa19h0eq', user='pesbjowuflgiha')
# #   # import urlparse, psycopg2
# #   # urlparse.uses_netloc.append('postgres')
# #   # url = urlparse.urlparse(os.environ["DATABASE_URL"])
#   db = PostgresqlDatabase(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
#   models.initialize()
# # else:
# #   db = SqliteDatabase('fresh.db')
# #   DATABASE.initialize(db)

class User(UserMixin, Model):
  username = CharField(unique=True)
  email = CharField(unique=True)
  password  = CharField(max_length=100)
  joined_at = DateTimeField(default=datetime.datetime.now)
  is_admin = BooleanField(default=False)

  class Meta:
    database = DATABASE
  
  def get_posts(self):
    return Post.select().where(Post.user == self)

  def get_stream(self):
    return Post.select().where(
      (Post.user == self)
    )
    
  @classmethod
  def create_user(cls, username, email, password, admin=False):
    try:
      cls.create(
        username=username,
        email=email,
        password=generate_password_hash(password),
        is_admin=admin
      )
    except IntegrityError:
      raise ValueError("User already exists")

class Barber(Model):
  name = CharField()
  neighborhood = CharField()
  profile_pic = CharField()
  portfolio_pic = CharField()

  class Meta:
    database = DATABASE

#############################################################
#################### Review Model Methods ###################
#############################################################

class Review(Model):
  timestamp = DateTimeField(default=datetime.datetime.now)
  barber = ForeignKeyField(Barber, backref='reviews')
  user_id = ForeignKeyField(User, backref='reviews')
  text = TextField()
  rating = CharField()

  class Meta:
    database = DATABASE
    order_by = ('-timestamp',)

class Post(Model):
  timestamp = DateTimeField(default=datetime.datetime.now)
  user = ForeignKeyField(
    model=User,
    backref='posts'
  )
  content = TextField()

  class Meta:
    database = DATABASE
    order_by = ('-timestamp',)

def initialize():
  DATABASE.connect()
  DATABASE.create_tables([User, Barber, Review, Post], safe=True)
  DATABASE.close()