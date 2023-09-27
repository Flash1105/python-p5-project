from flask_sqlalchemy import SQLAlchemy
from server.database import db

class SpeciesProfile(db.Model):
    __tablename__ = 'species_profiles'

    profile_id = db.Column(db.Integer, primary_key=True)
    species_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)