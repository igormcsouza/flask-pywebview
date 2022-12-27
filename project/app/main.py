"""Main application.

Because this is a proof of concept, the main page does nothing except place the
button to logout the user. The `/` route is protected though, user must be
logged in first.

Typical usage example:

    curl -X GET -b cookies.txt http://host:port/
"""
from flask import Flask, Blueprint, render_template
from flask_login import login_required, current_user


bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("", methods=["GET"])
@login_required
def main():
    """Main page of the application.

    Say the name of the authenticated user and place the logout button.

    Returns:
        The main page or redirect to login if no users were logged in yet.

    """
    return render_template("main/index.html", name=current_user.name)


def init_app(app: Flask):
    """Initialize the blueprint.

    Register the bluprint under app.

    Args:
        app: Flask: The created flask application.

    """
    app.register_blueprint(bp)
