from app import app

@app.route("/")
def index():
    return "Hello World"

@app.route("/<name>")
def greet(name):
    return f"Hello {name}"

@app.route("/<name>/<hello>")
def haha(name, hello):
    return f"Hi {name}, Your fav color is {hello}"