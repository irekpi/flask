from adoption import db
from flask import render_template, redirect, request, url_for, flash, abort, Blueprint
from flask_login import login_user, login_required, logout_user
from adoption.models import User
from .forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash

account_blueprints = Blueprint('account',
                              __name__,
                              template_folder='templates/account')


@account_blueprints.route('/welcome')
# @login_required
def welcome_user():
    return render_template('welcome.html')


@account_blueprints.route('/logout')
# @login_required
def logout():
    logout_user()
    flash('You are logged out!')
    return redirect(url_for('index'))


@account_blueprints.route('/login')
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('You logged in')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('welcome_user')

            return redirect(next)
    return render_template('login.html', form=form)


@account_blueprints.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You created and account')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)