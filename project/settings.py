"""Resides the settings module.

The settings for all the diferent behaviors we looking for (test and
development scenarios). Usually most of the information here is read from
environment variables, but this is a proof of concept and security is not an
issue. Becareful otherwise.

Typical usage example:

    from project.settings import TestConfig

    # creation of the app
    app.config.from_object(TestConfig)
"""
from datetime import timedelta
from abc import ABC
from typing import Type


class SettingConfigException(Exception):
    """Exception to be raised if no Settings is available with the given name.

    Attributes:
        env: Name of the settings one is looking for.
        message: What to show to user, defaults to a message that explain that
            `env` was not found.

    """

    def __init__(
        self, env, message="The given env %s is not a valid configuration"
    ):
        """Initialize the Exception."""
        self.env = env
        self.message = message
        super().__init__(self.message % env)


class BaseConfig(ABC):
    """Represents the basic configuration.

    All the configurations the others have in common.
    """

    # Database Configurations
    SECRET_KEY = "mysupersecrectpassphrase"  # noqa


class DevelopmentConfig(BaseConfig):
    """Store the development configurations.

    All the configurations that are meant to be used when a new instance of
    flask is created.
    """

    ENV = "development"

    # Database Configurations
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"

    # Flask_Login Configurations
    PERMANENT_SESSION_LIFETIME = timedelta(seconds=30)


class TestConfig(BaseConfig):
    """Store the test configurations.

    Configurations for testing the application, for example, the database is
    best to be in memory for this one.
    """

    ENV = "test"

    # Database Configurations
    SQLALCHEMY_DATABASE_URI = "sqlite://"


configurations = {"development": DevelopmentConfig, "test": TestConfig}


def choose_config(env: str) -> Type[BaseConfig]:
    """Choose what configuration is needed according to the env variable.

    Give back to the user the configuration according to the environment the
    application is.

    Returns:
        One class of type BasicConfig according to the environment.

    Raises:
        SettingConfigException: The given env %s is not a valid configuration.

    """
    try:
        config = configurations[env]
    except KeyError as e:
        raise SettingConfigException(env) from e

    return config
