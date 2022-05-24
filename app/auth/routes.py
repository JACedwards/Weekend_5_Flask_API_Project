from flask import Blueprint, render_template, request, redirect, url_for, flash

auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth', static_folder = 'auth_static')

from .authforms import LoginForm, RegistrationForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    lform = LoginForm()
    if request.method == 'POST':
        if lform.validate_on_submit():

            username = lform.username.data
            password = lform.password.data
            print('formdata:', username, password)
            flash(f"{username}, You have successfully signed in!", category = 'success')
            return redirect(url_for('home'))
        
        else:
            return redirect(url_for('auth.login'))

    return render_template('signin.html', form=lform)





@auth.route('/register', methods=['GET', 'POST'])
def register():
    # utilize our form for both GET and POST
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # check db
            # access form data
            print(form.data) # all data as a dict
            print(form.email.data) # specifically the data of the email field
            flash('Welcome! Thank you for registering!', 'info')
            return redirect(url_for('home'))
        else: # something went wrong with registration
            flash('Sorry, passwords do not match. Please try again.', 'danger')
            return redirect(url_for('auth.register'))
    elif request.method == 'GET':
        return render_template('register.html', form=form)