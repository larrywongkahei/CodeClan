from app import app
from flask import render_template, request
from models.list_event import events,Event, add, remove

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/views")
def event():
    return render_template("events.html", events=enumerate(events, 1))

@app.route("/views/add")
def form_page():
    return render_template("new_plan.html")

@app.route("/views/remove")
def delete_page():
    return render_template("remove.html", events=events)

@app.route("/views/remove", methods=["POST"])
def delete():
    list = []
    for item in events:
        name_to_delete = request.form.keys()
        if item.name in name_to_delete:
            list.append(item)
    for i in list:
        remove(i)
    return render_template("events.html")
    
    
        

@app.route("/views", methods=["POST"])
def add_plan():
    form_data = request.form
    name = form_data["eventname"]
    date = form_data["date"]
    number = form_data["number"]
    location = form_data["location"]
    description = form_data["description"]

    new_plan = Event(date, name, number, location, description)

    add(new_plan)
    return render_template("events.html")


