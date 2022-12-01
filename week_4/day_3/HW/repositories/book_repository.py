from models.books import Book
from db.run_sql import run_sql
from repositories import author_repository

def save(book):
    sql = "INSERT INTO books (title, years, price, author_id) VALUES (%s, %s, %s, %s) RETURNING *"
    VALUES = [book.title, book.years, book.price, book.author.id]
    result = run_sql(sql, VALUES)
    if result:
        result = result[0]
        book.id = result['id']

def select_all():
    sql = "SELECT * FROM books"
    VALUES = []
    result = run_sql(sql, VALUES)
    books = []
    for book in result:
        author = author_repository.select_by_id(book['author_id'])
        book1 = Book(book['title'], book['years'], book['price'], author, book['id'])
        books.append(book1)
    return books

def select_by_id(id):
    sql = "SELECT * FROM books WHERE id = %s"
    VALUES = [id]
    result = run_sql(sql, VALUES)
    if result :
        result = result[0]
        author = author_repository.select_by_id(result['author_id'])
        book = Book(result['title'], result['years'], result['price'], author, result['id'])
        return book
    return None

def delete_by_id(id):
    sql = "DELETE FROM books WHERE id = %s"
    VALUES = [id]
    run_sql(sql,VALUES)

def update(title, years, price, author_id, id):
    sql = "UPDATE books SET (title, years, price, author_id) = (%s, %s, %s, %s) WHERE id = %s RETURNING *"
    values = [title, years, price, author_id, id]
    run_sql(sql, values)

def select_by_author_name(author):
    sql = "SELECT * FROM books WHERE author.name = %s"
    values = [author]
    book = run_sql(sql, values)
    return book

def select_by_name(name):
    sql = "SELECT * FROM books WHERE name = %s"
    VALUES = [name]
    result = run_sql(sql, VALUES)
    if result:
        result = result[0]
        book = Book(result['title'], result['years'], result['price'], result['author'])
        return book
    return None