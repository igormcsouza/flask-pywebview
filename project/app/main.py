from flask import Flask, Blueprint, render_template
from flask_login import login_required, current_user


bp = Blueprint("main", __name__, url_prefix='/')


@bp.route('', methods=["GET"])
@login_required
def main():
    return render_template('main/index.html', name=current_user.name)


def init_app(app: Flask):
    app.register_blueprint(bp)
