from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import User, db
from werkzeug.security import check_password_hash
from flask_login import login_user, current_user, login_required, logout_user

auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth', static_folder = 'auth_static')

from .authforms import LoginForm, RegistrationForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    lform = LoginForm()
    if request.method == 'POST':
        if lform.validate_on_submit():

            print('formdata:', lform.username.data, lform.password.data)
            user = User.query.filter_by(username=lform.username.data).first()
            if user and check_password_hash(user.password, lform.password.data):
                login_user(user)
                print('current user:', current_user.__dict__)


                flash(f"{user.username}, You have successfully signed in!", category = 'success')
                return redirect(url_for('home'))
        

        flash(f"Incorrect username or password. Please try again", 'danger')
        return redirect(url_for('auth.login'))

    return render_template('signin.html', form=lform)





@auth.route('/register', methods=['GET', 'POST'])
def register():
    # utilize our form for both GET and POST
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # access form data and use it to create a new user object
            print('formdata:', form.data) # all data as a dict
            newuser = User(form.username.data, form.email.data, form.password.data, form.first_name.data, form.last_name.data)
            print('newly created user object:', newuser)
            try:
                # check db to see if this username or email already exists (use try/except)
                db.session.add(newuser)
                db.session.commit()
            except:
                flash('Username or email already registered! Please try a different one.', category='danger')
                return redirect(url_for('auth.register'))
            # log in the new user
            login_user(newuser)
            flash(f'Welcome! Thank you for registering, {newuser.username}!', 'info')
            return redirect(url_for('home'))
        else: # something went wrong with registration
            flash('Sorry, passwords do not match. Please try again.', 'danger')
            return redirect(url_for('auth.register'))
    # GET -> create form instance, then rendering the hmtl template with that form
    elif request.method == 'GET':
        return render_template('register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully loggedout.', 'info')
    return redirect(url_for('auth.login'))
