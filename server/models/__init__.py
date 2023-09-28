from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from server.models.user import User
from auth import bp as auth_bp
from server.config import Config
from server.database import db

migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    app.register_blueprint(auth_bp, url_prefix='/auth')
    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))