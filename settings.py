from datetime import timedelta


class BaseConfig(object):
    ...


class DevelopmentConfig(BaseConfig):
    ENV = "development"

    # Database Configurations
    SECRET_KEY = "mysupersecrectpassphrase"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"

    # Flask_Login Configurations
    REMEMBER_COOKIE_DURATION = timedelta(seconds=30)
    PERMANENT_SESSION_LIFETIME = timedelta(seconds=30)