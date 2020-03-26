import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

# DB ###
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# login

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


from puppy_company.core.views import core
from puppy_company.error_pages.handlers import error_pages
from puppy_company.users.views import users
from puppy_company.forum_post.views import forum_posts
app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(forum_posts)
app.register_blueprint(users)


