import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import User, Observation, Discussion, SpeciesProfile
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

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# ... (rest of your code)


@app.route('/')
def index():
    return '<h1>Project Server</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
