from flask_login import login_user, login_required, logout_user
from flask import Flask, Blueprint, redirect, url_for, request, flash, render_template, session
from werkzeug.security import generate_password_hash, check_password_hash

from tools.database.models import User


bp = Blueprint("auth", __name__, url_prefix='/auth')


@bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # retrieve login information
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') == 'on' else False

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash("Email or Password are incorrect, please, try again.", "error")
            return redirect(url_for("auth.login"))

        if not login_user(user, remember=remember):
            flash("Attempt to login failed for some reason!", "error")

        session.permanent = True
        return redirect(request.args.get('next') or url_for("main.main"))
    else:
        return render_template('auth/index.html')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


def init_app(app: Flask):
    app.register_blueprint(bp)