import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))


app1 = Flask(__name__)

app1.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app1)
Migrate(app1, db)


class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # one to many
    # Puppy to many Toys
    toys = db.relationship('Toy', backref='puppy', lazy='dynamic')
    #one to One
    #One Puppy to One Owner
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name{self.name} owner is {self.owner.name}"
        else:
            return f"Puppy {self.name}has no owner"

    def report_toys(self):
        print("thise are my toys:")
        for toy in self.toys:
            print(toy.item_name)


class Toy(db.Model):
    __tablename__ = 'toys'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppy.id'))

    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id


class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppy.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id
