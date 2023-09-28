from flask import render_template, Blueprint, redirect, url_for, session, flash
from . import bp  
from werkzeug.security import check_password_hash
from .forms import LoginForm, RegisterForm
from server.models.user import User
from server.database import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            session['user_id'] = user.user_id
            flash('You were successfully logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You were successfully logged out!', 'success')
    return redirect(url_for('main.index'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('You were successfully registered!', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred. Please try again later.', 'danger')
            print(e)  # For debugging purpose. In production, consider logging the error.
    return render_template('register.html', form=form)
