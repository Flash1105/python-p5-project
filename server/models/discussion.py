from flask_sqlalchemy import SQLAlchemy
from server.database import db

class Discussion(db.Model):
    __tablename__ = 'discussions'

    discussion_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    observation_id = db.Column(db.Integer, db.ForeignKey('observations.observation_id'), nullable=False)
    message = db.Column(db.Text, nullable=False)

    user = db.relationship('User', backref='discussion')
    observation = db.relationship('Observation', backref='discussion')