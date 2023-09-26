from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from server.database import db

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(64))
    
    # Hashing the password before saving
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    # Verifying the password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
