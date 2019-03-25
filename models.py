import datetime
import os
from peewee import *
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash
from playhouse.db_url import connect
from flask import g

# DATABASE = connect(os.environ.get('DATABASE_URL'))
DATABASE = PostgresqlDatabase('fresh') #local postgres backup
# DATABASE = SqliteDatabase('fresh.db') #local sqlitebackup if postgres is buggy

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