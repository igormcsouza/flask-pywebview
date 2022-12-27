"""The base of the SQLAlchemy database.

Initialize the database and create all the models. In order to avoid circular
import, the init_app has to be called from the __init__.py, otherwise, if
called from here, the Model might not be loaded yet, causing error. If
importing the Models here, then a circular import will occur because Models
uses db too.

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app: Flask):
    """Initialize the database and create the tables.

    Add the app to the database, get the configurations and initialize all the
    tables if needed.

    Args:
        app: Flask: The created flask application.

    """
    db.init_app(app)

    with app.app_context():
        db.create_all()
