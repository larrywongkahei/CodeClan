from repositories import author_repository, book_repository
from models.author import Author
from models.books import Book

author1 = Author('Larry', 22, 'M')
author_repository.save(author1)
author2 = Author('Tim', 18, "M")
author_repository.save(author2)

book1 = Book('little prince', '2018', 2000, author1)
book_repository.save(book1)
book2 = Book('How to pet', '2022', 2500, author1)
book_repository.save(book2)
book3 = Book('Dont know how to do', '2019', 500, author2)
book_repository.save(book3)

print(author1.id)
print(book1.id)