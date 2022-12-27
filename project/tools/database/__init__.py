"""Database Abstraction.

The main stuff here is the User model and the db variable used to do the
database stuff. Other classes and modules come here to get those informations.
It is necessary to have User here because it must be imported before init_app
be executed, so, when creating the app, the user will import init_app from here
and the User will be available.

Typical usage example:

    from project.tools import database

    # creation of the app
    database.init_app(app)
"""
from project.tools.database.models import User
from project.tools.database.base import init_app, db
