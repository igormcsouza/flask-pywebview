import pytest

from project.starter import create_app
from project.tools.database import db


@pytest.fixture()
def app():
    app = create_app(env="test")

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
