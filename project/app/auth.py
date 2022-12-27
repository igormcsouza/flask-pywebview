"""Authenticates a user and log him out.

The two main views here are the `/login` and `/logout`, to access the logout
one must be logged in first. The process of log in and out is done through
caching cookies on the browser.

Typical usage example:

    curl -X POST -c cookies.txt \
        -d "email=your_email&password=your_password&remember=1" \
        http://host:port/login
    curl -X GET -b cookies.txt http://host:port/logout
"""
from flask_login import login_user, login_required, logout_user
from flask import (
    Flask,
    Blueprint,
    redirect,
    url_for,
    request,
    flash,
    render_template,
    session,
)
from werkzeug.security import check_password_hash

from project.tools.database.models import User


bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["GET", "POST"])
def login():
    """Logs subscribed users in.

    Given a real user (on the database) logs in.

    Returns:
        Redirect to the main page or follows the page which was waiting the log
        in if everything works out. Reroutes to login again otherwise.

    Raises:
        RetrieveDataError: If no user is found. Reroutes to login.

    """
    if request.method == "POST":
        # retrieve login information
        email = request.form.get("email")
        password = request.form.get("password")
        remember = request.form.get("remember") == "on"

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash(
                "Email or Password are incorrect, please, try again.", "error"
            )
            return redirect(url_for("auth.login"))

        if not login_user(user, remember=remember):
            flash(
                "Attempt to login failed for some reason!", "error"
            )  # pragma: no cover  # noqa
            return redirect(url_for("auth.login"))  # pragma: no cover

        session.permanent = True
        return redirect(request.args.get("next") or url_for("main.main"))

    return render_template("auth/index.html")


@bp.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logs out the subscribed.

    In general, it checks if the user is authenticated, if yes, destroy the
    cookie and redirects to the login page.

    Returns:
        Redirect to the login page, it does also redirect to login if no users
        are authenticated.

    """
    logout_user()
    return redirect(url_for("auth.login"))


def init_app(app: Flask):
    """Initialize the blueprint.

    Register the bluprint under app.

    Args:
        app: Flask: The created flask application.

    """
    app.register_blueprint(bp)
