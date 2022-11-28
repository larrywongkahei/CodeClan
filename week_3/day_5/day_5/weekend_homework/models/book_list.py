from models.book import Book

book1 = Book("Harry Potter", "J K Rowling", "Fictional", False)
book2 = Book("No Plan B", "Jack Reacher", "non-Fictional", False)
book3 = Book("Killing Floor", "Jack Reacher", "Fictional", False)

books = [book1, book2, book3]

def add_book(book):
    books.append(book)

def removebook(books, delete_data):
    for book in get_checked_books_list(books, delete_data):
        books.remove(book)

def get_checked_books_list(book_list, form_data):
    list = []
    for book in book_list:
        if book.title in form_data:
            list.append(book)
    return list

def check_in_or_out(book_list, data):
    for book in book_list:
        if book.title in data:
            if book.check_out:
                book.check_out = False
            else:
                book.check_out = True
