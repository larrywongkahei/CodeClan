from models.book import Book

book1 = Book("Harry Potter", "J K Rowling", "Fictional", False)
book2 = Book("No Plan B", "Jack Reacher", "non-Fictional", False)
book3 = Book("Killing Floor", "Jack Reacher", "Fictional", False)

books = [book1, book2, book3]

def add_book(book):
    books.append(book)

def removebook(book):
    books.remove(book)