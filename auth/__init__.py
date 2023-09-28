from flask import Blueprint
from flask_login import LoginManager


login_manager = LoginManager()


bp = Blueprint('auth', __name__)

from .routes import auth_bp