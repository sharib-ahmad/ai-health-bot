from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, login_required, current_user
from models.forms import LoginForm, RegisterForm
from models import db, login_manager
from models.model import User
import random

auth_bp = Blueprint("auth_bp", __name__, template_folder="../templates")


# Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Route: Register
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("bot_bp.chat"))

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=(form.email.data).strip())
        user.username = '@' + (form.email.data).strip().split('@')[0] + str(random.randint(100,999))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully! Please login.", "success")
        current_app.logger.info("New user registered: %s", user.email)
        return redirect(url_for("auth_bp.login"))
    
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {field}: {error}", "danger")
                current_app.logger.error("Error in form field: %s", error)

    return render_template("auth/register.html", form=form)


# Route: Login
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("bot_bp.chat"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(f"Welcome, {user.email}!", "success")
            current_app.logger.info("User logged in: %s", user.email)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("bot_bp.chat"))
        else:
            flash("Invalid email or password.", "danger")
            current_app.logger.error("Failed login attempt: %s", form.email.data)
    return render_template("auth/login.html", form=form)


# Route: Logout
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth_bp.login"))
