from app import app
from modles.order import orders
from flask import render_template


@app.route("/orders")
def view_all_order():
    return render_template("index.html", orders=orders)

@app.route("/orders/<int:index>")
def view_one_order(index):
    return render_template("order.html", order=orders[index])