from server.models import db
from flask_login import UserMixin

class SpeciesProfile(db.Model):
    __tablename__ = 'species_profiles'

    profile_id = db.Column(db.Integer, primary_key=True)
    species_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)