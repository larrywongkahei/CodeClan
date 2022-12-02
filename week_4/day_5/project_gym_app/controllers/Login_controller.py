from flask import Flask, render_template, Blueprint


# Set a login blueprint to make it easier to debug.
Login_blueprint = Blueprint("Login", __name__)