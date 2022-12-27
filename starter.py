from flask import Flask, redirect

from app import auth, main
from tools import database, safeguard
from settings import BaseConfig, DevelopmentConfig


def create_minimal_app(setting: BaseConfig) -> Flask:
    app = Flask(__name__)
    app.config.from_object(setting)

    return app


def create_app() -> Flask:
    app = create_minimal_app(DevelopmentConfig)

    # Initialize infrastructure
    database.init_app(app)
    safeguard.init_app(app)

    # Initialize project blueprints
    auth.init_app(app)
    main.init_app(app)

    return app
