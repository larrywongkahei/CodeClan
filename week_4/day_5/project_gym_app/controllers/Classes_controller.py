from flask import Flask, render_template, Blueprint

# Set a classes blueprint to make it easier to debug.
classes_blueprint = Blueprint("classes", __name__)