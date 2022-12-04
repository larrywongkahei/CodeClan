from flask import render_template, Blueprint
from repositries import classes_repository
from repositries import members_repository
from repositries import class_attend_repositry
from repositries import admin_repository

admin_blueprint = Blueprint("admin", __name__)

@admin_blueprint.route("/admin")
def admin_homepage():
    classes = classes_repository.check_class_today()
    members = members_repository.check_today_member(classes)
    members_classes = admin_repository.print_all_class_member_today(classes)


    return render_template("admin/index.html", classes=classes, members=members, dict_list =  members_classes)

