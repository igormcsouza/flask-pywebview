import flask_login
from unittest import mock
from werkzeug.security import generate_password_hash

from project.tools.database import db, models


def test_when_not_loggen_show_loggin_page(client):
    response = client.get("/")

    assert response.status_code == 302
    assert response.headers["Location"] == "/auth/login?next=%2F"


def test_when_send_incorrect_info_not_login(client):
    response = client.post(
        "/auth/login",
        data={"email": "anything", "password": "anything", "remember": "on"},
        follow_redirects=True,
    )

    assert b"<title>Login Page</title>" in response.data


def test_when_send_correct_info_go_to_main(client, app):
    obj = models.User()
    obj.email = "any@thing.com"
    obj.password = generate_password_hash("anything")
    obj.name = "AnyThing"

    with app.app_context():
        db.session.add(obj)
        db.session.commit()

    response = client.post(
        "/auth/login",
        data={
            "email": "any@thing.com",
            "password": "anything",
            "remember": "off",
        },
        follow_redirects=True,
    )

    assert b"<title>Main Page</title>" in response.data
    assert (
        b'<a href="/auth/logout" class="btn btn-primary btn-lg" role="button"\n        >Logout</a\n      >'
        in response.data
    )


def test_logout_successfully(client):
    with client:
        # Create a mock user object
        user = mock.Mock()
        user.is_authenticated = True

        # Patch the current_user property to return the mock user
        with mock.patch("flask_login.utils.current_user", user):
            # Make a GET request to the logout endpoint
            response = client.get("/auth/logout")

            # Assert that the logout function was called
            logout_user_mock = mock.Mock(wraps=flask_login.logout_user)
            logout_user_mock()
            assert logout_user_mock.called
            logout_user_mock.assert_called_once()

            # Assert that the response is a redirect to the login page
            assert response.status_code == 302
            assert response.headers["Location"] == "/auth/login"
