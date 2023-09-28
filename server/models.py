## probably garbage! ##

from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(64))
    observtion = db.relationship('Observation', backref='user', lazy='dynamic')
    discussion = db.relationship('Discussion', backref='user', lazy='dynamic')

    # Used to set hashed password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Used to check hashed password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Observation(db.Model):
    __tablename__ = 'observations'

    observation_id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(64))
    location = db.Column(db.String(64))
    behavior = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    images = db.Column(db.String(128))
    discussion = db.relationship('Discussion', backref='observation', lazy='dynamic')
    create_at = db.Column(db.DateTime, default=datetime.now)


class Discussion(db.Model):
    __tablename__ = 'discussions'

    discussion_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    observation_id = db.Column(db.Integer, db.ForeignKey('observations.observation_id'))
    message = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.now)

class SpeciesProfile(db.Model):
    __tablename__ = 'species_profiles'

    profile_id = db.Column(db.Integer, primary_key=True)
    species_name = db.Column(db.String(64))
    description = db.Column(db.String(128))
    images = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.now)