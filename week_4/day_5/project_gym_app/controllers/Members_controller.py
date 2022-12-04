from flask import Flask, render_template, Blueprint

# Set a members blueprint to make it easier to debug.
members_blueprint = Blueprint("members", __name__)

# Show all the advantage to be a members
@members_blueprint.route("/members_privilege")
def show_members_privilege():
    return render_template