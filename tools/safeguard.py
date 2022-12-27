from flask import Flask
from flask_login import LoginManager

from tools.database.models import User


login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


def init_app(app: Flask):
    login_manager.init_app(app)
