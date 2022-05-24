import os

basedir = os.path.abspath(os.path.dirname(__name__))

class Config:
    """ setting configuration variables telling Flask how to run"""

    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


