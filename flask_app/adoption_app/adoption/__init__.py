import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


login_manager = LoginManager()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# SQL DB
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)

from adoption.puppies.views import puppies_blueprints
from adoption.owners.views import owners_blueprints
from adoption.account.views import account_blueprints

app.register_blueprint(owners_blueprints, url_prefix='/owners')
app.register_blueprint(puppies_blueprints, url_prefix='/puppies')
app.register_blueprint(account_blueprints, url_prefix='/account')

# login
login_manager.init_app(app)
login_manager.login_view = 'login'