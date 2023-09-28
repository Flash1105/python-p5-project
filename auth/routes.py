from flask import render_template, Blueprint, redirect, url_for, session, flash, request, redirect, url_for
from . import bp  
from werkzeug.security import check_password_hash
from .forms import LoginForm, RegisterForm
from server.models.user import User
from server.database import db
from flask_login import login_required, login_user, logout_user
from server.models.observation import Observation
from server.models.discussion import Discussion
from flask_login import login_manager
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('You were successfully logged in!', 'success')
            return redirect(url_for('templates.dashboard'))
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
    print("Register route hit")
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            print("User added to the database:", user)
            flash('You were successfully registered!', 'success')
            login_user(user)
            return redirect(url_for('auth.dashboard'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred. Please try again later.', 'danger')
            print("Error", e)
    else:
        print("form not validated", form.errors)

    return render_template('register.html', form=form)

@auth_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

observation_bp = Blueprint('observation', __name__)

# display list of observations
@observation_bp.route('/observations')
def observations():
    obs_list = Observation.query.all()
    return render_template('observations.html', observations=obs_list)

@observation_bp.route('/observation/<int:obs_id>', methods=['GET', 'POST'])
def observation_detail(obs_id):
    observation = Observation.query.get(obs_id)
    if request.method == 'POST':
        message = request.form.get('message')
        if message: 
            discussion = Discussion(message=message, user_id=session['user_id'], observation_id=obs_id)
            db.session.add(discussion)
            db.session.commit()
            flash ('Discussion added successfully!', 'success')
            return redirect(url_for('observation.observation_details', obs_id=obs_id))

    discussions = Discussion.query.filter_by(observation_id=obs_id).all()
    return render_template('observation_detail.html', observation=observation, discussions=discussions)

@observation_bp.route('/observations/new', methods=['GET', 'POST'])
def new_observation():
    if request.method =='POST':
        species = request.form['species']
        location = request.form['location']
        behavior = request.form['behavior']
        user_id = session['user_id']
        images = request.form['images']
        new_observation = Observation(species=species, location=location, behavior=behavior, user_id=user_id, images=images)
        db.session.add(new_observation)
        db.session.commit()
        return redirect(url_for('observation.observations'))
    return render_template('new_observation.html')

