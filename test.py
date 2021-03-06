#coding=utf8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://leo:Wahrr7231657@198.35.45.184:3306/blog'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True)
    email = db.Column(db.String(120), unique = True)

    def __init__(self, username, email):
        self.username, self.email = username, email

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category_id'))
    category = db.relationship('Category', 
                               backref = db.backref('posts', lazy = 'dynamic'))

    def __init__(self, title, body, category, pub_date = None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
            self.pub_date = pub_date
            self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

class Kls(object):
    no_inst = 0

    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1

    @classmethod
    def get_no_of_instance(cls_obj):
        return cls_obj.no_inst

ik1 = Kls()
ik2 = Kls()

print ik1.get_no_of_instance()
print Kls.get_no_of_instance()

class He(object):
    no_inst = 0

    def __init__(self):
        self.no_inst += 1

    def inc(self):
        He.no_inst += 1
