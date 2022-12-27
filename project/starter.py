"""The starter of the module, where the main APP is created.

Here is create the APP and delivered as a response of the create_app function.

Typical usage example:

    from project.starter import create_app

    app = create_app(env=development)
"""
from typing import Type

from flask import Flask

from project.app import auth, main
from project.tools import database, safeguard
from project.settings import BaseConfig, choose_config


def create_minimal_app(setting: Type[BaseConfig]) -> Flask:
    """Creates a minimal app, usually for testing.

    This minimal app has nothing but the basic configuration and the starter
    app, no new addition is made at this point.

    Args:
        settings: type[BaseConfig]: Gets a configuration the inherits from
            BaseConfig.

    Returns:
        The minimal Flask App created.

    """
    app = Flask(__name__)
    app.config.from_object(setting)

    return app


def create_app(env: str = "development") -> Flask:
    """Creates the actual application.

    It gets the minimal app created before and install all the new tools and
    blueprints it needs. It is the actual application.

    Args:
        env: str: The enviroment the application resides, usually `development`
            or `test`.

    Returns:
        The Flask App created.

    """
    app = create_minimal_app(choose_config(env))

    # Initialize infrastructure
    database.init_app(app)
    safeguard.init_app(app)

    # Initialize project views
    auth.init_app(app)
    main.init_app(app)

    return app
