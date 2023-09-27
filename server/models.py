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
    locaation = db.Column(db.String(64))
    behavior = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    images = db.Column(db.String(128))

class Discussion(db.Model):
    __Tablename__ = 'discussions'

    discussion_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    observation_id = db.Column(db.Integer, db.ForeignKey('observations.observation_id'))
    mssage = db.Column(db.String(128))

class SpeciesProfile(db.Model):
    __tablename__ = 'species_profiles'

    profile_id = db.Column(db.Integer, primary_key=True)
    species_name = db.Column(db.String(64))
    description = db.Column(db.String(128))
    images = db.Column(db.String(128))