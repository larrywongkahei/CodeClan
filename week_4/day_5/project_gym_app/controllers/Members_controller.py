from flask import Flask, render_template, Blueprint

# Set a members blueprint to make it easier to debug.
members_blueprint = Blueprint("members", __name__)