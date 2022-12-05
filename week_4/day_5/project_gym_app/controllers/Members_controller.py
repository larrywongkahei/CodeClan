from flask import Flask, render_template, Blueprint
from repositries import members_repository

# Set a members blueprint to make it easier to debug.
members_blueprint = Blueprint("members", __name__)

# Show all the advantage to be a members
@members_blueprint.route("/members_privilege")
def show_members_privilege():
    return render_template

@members_blueprint.route("/checkin/<member_name>")
def checkin(member_name):
    members_repository.check_in(member_name)
    return render_template("members/checkin.html", checkin=True)