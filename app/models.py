from re import S
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask_login import LoginManager, UserMixin
login = LoginManager()

@login.user_loader
def load_user(userid):
    return User.query.get(userid)

from datetime import datetime
from uuid import uuid4
from werkzeug.security import generate_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.String(40), primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    created = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, username, email, password, first_name='', last_name=''):
        self.username = username
        self.email = email.lower()
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid4())
        self.password = generate_password_hash(password)



class Animal(db.Model):
    id = db.Column(db.String, primary_key=True) 
    species = db.Column(db.String(50), nullable=False)
    latin_name = db.Column(db.String(255), default=None)
    size_cm = db.Column(db.Integer)
    diet = db.Column(db.String(255))
    lifespan = db.Column(db.String(255))
    description = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), default=None)
    price = db.Column(db.Float(2), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, dict):
        #required
        self.id = str(uuid4())
        self.species=dict['species'].title()
        self.description = dict['description']
        self.price = dict['price']
        #optional
        self.image = dict.get('image')
        self.size = dict.get('size_cm', 0)
        self.latin_name = dict.get('latin_name', 'unknown')
        self.diet = dict.get('diet', 'unknown')
        self.lifespan = dict.get('lifespan', 0)

    def to_dict(self):
        return {
        'id': self.id,  
        'species': self.species, 
        'latin_name': self.latin_name, 
        'size_cm' : self.size_cm, 
        'diet': self.diet, 
        'lifespan': self.lifespan, 
        'description': self.description, 
        'image': self.image, 
        'price': self.price, 
        'created_on': self.created_on, 

        }



