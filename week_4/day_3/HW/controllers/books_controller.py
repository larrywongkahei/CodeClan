from flask import Flask, Blueprint, render_template, request, redirect
from repositories import book_repository


books_bp = Blueprint("books", __name__)

@books_bp.route("/books")
def show_all_books():
    books = book_repository.select_all()
    return render_template("books/books.html", books=books)

@books_bp.route("/<book_id>")
def show_book(book_id):
    book = book_repository.select_by_id(book_id)
    return render_template("books/book.html", book=book)

@books_bp.route("/delete")
def delete_page():
    books = book_repository.select_all()
    return render_template("books/delete.html", books=books)

@books_bp.route("/books", methods=["POST"])
def delete_book():
    data = request.form.keys()
    books = book_repository.select_all()
    for book in books:
        if book.title in data:
            book_repository.delete_by_id(book.id)
    return render_template("index.html")