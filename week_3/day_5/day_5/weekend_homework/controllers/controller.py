from app import app
from flask import render_template, request
from models.book_list import books, add_book, removebook, get_checked_books_list, check_in_or_out
from models.book import Book

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/booklist")
def showlist():
    return render_template("booklist.html", books=enumerate(books))

@app.route("/booklist/<int:index>")
def showbook(index):
    seleted_book = books[index]
    return render_template("book.html", book=seleted_book)

@app.route("/booklist/addbook")
def addbook_page():
    return render_template("addbook.html")

@app.route("/booklist", methods=["POST"])
def addbook():
    new_book_data = request.form
    title = new_book_data["title"]
    author = new_book_data["author"]
    genre = new_book_data["genre"]

    new_book = Book(title, author, genre, False)

    add_book(new_book)

    return render_template("booklist.html")

@app.route("/booklist/removebook")
def remove_page():
    return render_template("removebook.html", books=books)


@app.route("/booklist/removebook", methods=["POST"])
def remove_book():
    delete_data = request.form.keys()
    removebook(books, delete_data)

    return render_template("booklist.html")

@app.route("/booklist/changestatus")
def change_status():
    return render_template("changestatus.html", books=books)

@app.route("/booklist/changestatus", methods=["POST"])
def change():
    data = request.form.keys()
    check_in_or_out(books, data)
    return render_template("booklist.html")


