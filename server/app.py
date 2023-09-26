import os
from flask import Flask
from flask_migrate import Migrate
from database import db

app = Flask(__name__)

# Define the base directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Check if the directory exists and if not, create it
db_directory = os.path.join(BASE_DIR, 'data')
if not os.path.exists(db_directory):
    os.makedirs(db_directory)

# Configure the SQLAlchemy Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(db_directory, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


# Importing models here after initializing db to avoid circular import issues
from models.user import User
from models.observation import Observation
from models.discussion import Discussion
from models.species_profile import SpeciesProfile

@app.route('/')
def index():
    return '<h1>Project Server!!</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
