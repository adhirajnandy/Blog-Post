import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)

##### DATABASE SETUP ##########
basedir = os.path.abspath(os.path.dirname(__file__ ))
app.config['SECRET_KEY']='mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMT_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
Migrate(app,db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

from Company.core.views import core
from Company.error_pages.handlers import error_pages
from Company.users.views import users
from Company.blog_posts.views import blog_posts

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(blog_posts)