from flask import Flask

from project.app import auth, main
from project.tools import database, safeguard
from project.settings import BaseConfig, choose_config


def create_minimal_app(setting: BaseConfig) -> Flask:
    app = Flask(__name__)
    app.config.from_object(setting)

    return app


def create_app(env: str = "development") -> Flask:
    app = create_minimal_app(choose_config(env))

    # Initialize infrastructure
    database.init_app(app)
    safeguard.init_app(app)

    # Initialize project blueprints
    auth.init_app(app)
    main.init_app(app)

    return app
