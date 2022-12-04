from flask import Flask, render_template, Blueprint, request, redirect


# Set a login blueprint to make it easier to debug.
Login_blueprint = Blueprint("Login", __name__)

@Login_blueprint.route("/login")
def login_page():
    return render_template("login/login.html")

@Login_blueprint.route("/login", methods=['POST'])
def login():
    data = request.form
    if data['username'].lower() == "admin" and data['password'].lower() == "admin":
        return redirect("/admin")