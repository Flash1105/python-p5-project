import os
from flask import Flask, render_template
from flask_migrate import Migrate
from server.database import db
from auth.routes import auth_bp, observation_bp

app = Flask(__name__, template_folder='../templates')
app.register_blueprint(auth_bp, url_prefix='/auth.')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_default_key')
app.register_blueprint(observation_bp, url_prefix='/observation')
# Define the base directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Check if the directory exists and if not, creat it
db_directory = os.path.join(BASE_DIR, 'data')
if not os.path.exists(db_directory):
    os.makedirs(db_directory)

# Configure the SQLAlchemy Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(db_directory, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
