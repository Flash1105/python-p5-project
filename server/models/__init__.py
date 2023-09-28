from flask import Flask
from auth import bp as auth_bp
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    login_manager.init_app(app)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    return app
