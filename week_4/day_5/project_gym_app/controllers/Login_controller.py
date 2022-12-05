from flask import Flask, render_template, Blueprint, request, redirect, url_for
from repositries import members_repository
from models.members import Members


# Set a login blueprint to make it easier to debug.
Login_blueprint = Blueprint("Login", __name__)

@Login_blueprint.route("/login")
def login_page():
    return render_template("login/login.html")

@Login_blueprint.route("/login", methods=['POST'])
def login():
    data = request.form
    name = data['name']
    username = data['username'].lower()
    password = data['password'].lower()
    if username == "admin" and password == "admin":
        return redirect("/admin")
    try:
        members_repository.log_in(name, username, password)
    except:
        raise 
    else:
        return redirect(url_for('member', name=name))

@Login_blueprint.route("/signup")
def signup_page():
    return render_template("login/signup.html")

@Login_blueprint.route("/signup", methods=['POST'])
def signup():
    data = request.form
    name = data['name']
    username = data['username'].lower()
    password = data['password'].lower()
    members_repository.sign_up(name, username, password)
    return redirect(url_for("Login.signup_page2", name=name))

@Login_blueprint.route("/signup/<name>")
def signup_page2(name):
    return render_template("login/signup2.html", name=name)

@Login_blueprint.route("/signup/<name>", methods=['POST'])
def signup2(name):
    data = request.form
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    level = ["bronze", "silver", "gold", "platinum", "diamond"]
    gen = ["M", "F"]
    name = request.form['name']
    for lv in level:
        if lv in data:
            membership_level = lv

    for genders in gen:
        if genders in data:
            gender = genders
    
    availability = []
    for day in days:
        if day in data:
            availability.append(day)
    salary = data['salary']
    new_member = Members(name, membership_level, gender, availability, salary)
    members_repository.save(new_member)
    
    return redirect("/")
   


@Login_blueprint.route("/logout")
def logout():
    return render_template("/", login=False)
