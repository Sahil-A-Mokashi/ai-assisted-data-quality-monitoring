from flask import Blueprint, render_template, request, redirect, session
from database import db
from models import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    username = request.form["username"]
    password = request.form["password"]

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):

        session["username"] = user.username

        return redirect("/")

    return render_template(
        "login.html",
        error="Invalid username or password."
    )


@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect("/")