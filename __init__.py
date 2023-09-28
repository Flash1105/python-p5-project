from flask import Flask
from flask_login import LoginManager
from .auth import bp as auth_bp



login_manager = LoginManager()

def create_app():
    app= Flask(__name__)
    login_manager.init_app(app)
    app.register_blueprint(auth_bp, url_prefix='/auth.')
    return app