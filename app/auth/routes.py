from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='auth')

from .authforms import LoginForm

@auth.route('/signin')

def login():
    lform = LoginForm()
    return render_template('signin.html', form=lform)
