"""Define the User Model of the application.

The user model is used to save the information of the user to be logged in on
the application.

"""
from flask_login import UserMixin

from project.tools.database.base import db


class User(UserMixin, db.Model):  # type: ignore
    """User of the application.

    Attributes:
        id: int: Autocompletes by sqlalchemy.
        email: str: The user's email, should be its username.
        password: str: Stores the hash of the password.
        name: str: The name of the user.

    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
