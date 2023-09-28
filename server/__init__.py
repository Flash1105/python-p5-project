from flask import Flask
from flask_login import LoginManager
from server.config import Config
from server.database import db
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from server.models.user import User 
    return User.query.get(int(user_id))

def create_app(config_class=Config):
    template_path = '/home/flash1105/development/code/phase-5/python-p5-project-EntomoConnect/templates'
    app = Flask(__name__, template_folder=template_path)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)

    from auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
