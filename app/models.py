from re import S
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# setup login manager
from flask_login import LoginManager, UserMixin
# create the instance of our LoginManager
login = LoginManager()

# tell our login manager how it can access a User object from a user_id
@login.user_loader
def load_user(userid):
    return User.query.get(userid)

# tools for our models
from datetime import datetime
from uuid import uuid4
from werkzeug.security import generate_password_hash

# create a DB model -> aka a Python object that will be a table/entity in our SQL database
class Animal(db.Model):
    # global attributes for each column in the database
    id = db.Column(db.Integer, primary_key=True) # we need to provide at least a datatype (we can also provide default values and/or constraints)
    name = db.Column(db.String(50), nullable=False)
    latin = db.Column(db.String(255), default=None)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    cool = db.Column(db.Boolean, default=True) # i think
