from flask_sqlalchemy import SQLAlchemy
from server.database import db

class Observation(db.Model):
    observation_id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    behavior = db.Column(db.String(500), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
   