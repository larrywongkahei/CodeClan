from flask import Flask, Blueprint, render_template, request, redirect
from repositories import book_repository
from repositories import author_repository
from models.books import Book
from models.author import Author


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

@books_bp.route("/createbook")
def create_page():
    return render_template("books/create.html")

@books_bp.route("/createbook", methods=["POST"])
def create():
    data = request.form
    all_authors = author_repository.select_all()
    for author in all_authors:
        if author.name == data['author']:
            if author.age == data['author_age']:
                if author.gender == data['author_gender']:
                    the_author = author_repository.select_by_name(data['name'])
                    new_book = Book(data['title'], data['years'], data['price'], the_author)
                    book_repository.save(new_book)
                    return render_template("index.html")
    new_author = Author(data['author'], data['author_age'], data['author_gender'])
    author_repository.save(new_author)
    new_book = Book(data['title'], data['years'], data['price'], new_author)
    book_repository.save(new_book)
    return render_template("index.html")

@books_bp.route("/edit/<book_id>")
def edit_page(book_id):
    book = book_repository.select_by_id(book_id)
    return render_template("/books/edit.html", book=book)

@books_bp.route("/edit/<book_id>", methods=["POST"])
def edit(book_id):
    data = request.form
    the_book = book_repository.select_by_id(book_id)
    the_author = the_book.author
    book_repository.update(data['title'], data['years'], data['price'], the_author.id, the_book.id)
    return render_template("index.html")




