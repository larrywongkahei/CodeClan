from flask import Flask, render_template

app = Flask(__name__)

from controllers.Classes_controllers import classes_blueprint
from controllers.Members_controllers import members_blueprint

app.register_blueprint(classes_blueprint)
app.register_blueprint(members_blueprint)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)