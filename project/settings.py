from datetime import timedelta


class SettingConfigException(Exception):

    def __init__(self, env, message="The given env %s is not a valid configuration"):
        self.env = env
        self.message = message
        super().__init__(self.message % env)


class BaseConfig(object):
    ...


class DevelopmentConfig(BaseConfig):
    ENV = "development"

    # Database Configurations
    SECRET_KEY = "mysupersecrectpassphrase"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"

    # Flask_Login Configurations
    PERMANENT_SESSION_LIFETIME = timedelta(seconds=30)

class TestConfig(BaseConfig):
    ENV = "test"

    # Database Configurations
    SECRET_KEY = "mysupersecrectpassphrase"
    SQLALCHEMY_DATABASE_URI = "sqlite://"


def choose_config(env: str) -> BaseConfig:
    if env == "development":
        return DevelopmentConfig
    elif env == "test":
        return TestConfig

    raise SettingConfigException(env)
