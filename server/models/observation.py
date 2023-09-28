from flask_sqlalchemy import SQLAlchemy
from server.database import db

class Observation(db.Model):

    def __init__(self, species, location, behavior, user_id, images):
        self.species = species
        self.location = location
        self.behavior = behavior
        self.user_id = user_id
        self.images = images
        