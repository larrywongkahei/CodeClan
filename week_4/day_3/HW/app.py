from flask import Flask, render_template

app = Flask(__name__)

from controllers.books_controller import books_bp

app.register_blueprint(books_bp)


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)