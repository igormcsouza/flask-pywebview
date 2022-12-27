"""Basic configuration for Flask_Login.

Sets what is the login view and how to identify the user, it is used only for
Flask_Login to define itself. In the future must have all the fucntions and
decorators the application needs, so it won't need to import Flask_Login
itself.

"""
from typing import Union

from flask import Flask
from flask_login import LoginManager

from project.tools.database.models import User


login_manager = LoginManager()
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id: int) -> Union[User, None]:
    """Given the user id, queries for it and return the result.

    Give back to the user the configuration according to the environment the
    application is.

    Args:
        user_id: int: The ID of the user.

    Returns:
        An instance of User Model or None.

    """
    # since the user_id is just the primary key of our user table, use it in
    # the query for the user
    return User.query.get(int(user_id))


def init_app(app: Flask):
    """Initialize the security configurations for Flask_login.

    Add the add to the Flask_login instance.

    Args:
        app: Flask: The created flask application.

    """
    login_manager.init_app(app)
