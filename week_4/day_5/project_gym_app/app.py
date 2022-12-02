from flask import Flask, render_template

app = Flask(__name__)

# To import the blueprint from controllers file to register them
from controllers.Classes_controllers import classes_blueprint
from controllers.Members_controllers import members_blueprint

# To register blueprint
app.register_blueprint(classes_blueprint)
app.register_blueprint(members_blueprint)

# Set up a Home Page
@app.route("/")
def index():
    return render_template("index.html")

# To make sure functions only run on main page
if __name__ == "__main__":
    app.run(debug=True)