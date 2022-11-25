import unittest
from models.book import Book
from models import book_list

class Testfunction(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("Harry Potter", "J K Rowling", "Fictional", False)
        self.book2 = Book("No Plan B", "Jack Reacher", "non-Fictional", False)
        self.book3 = Book("Killing Floor", "Jack Reacher", "Fictional", False)
        book_list.books = [self.book1, self.book2, self.book3]
        self.book4 = Book("New book", "Larry", "Fictional", True)

    def test_add_boook(self):
        expected_outcome = 4
        book_list.add_book(self.book4)
        actual_outcome = len(book_list.books)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_remove_boook(self):
        expected_outcome = 2
        book_list.removebook(self.book3)
        actual_outcome = len(book_list.books)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_book_title(self):
        expected_outcome = "Harry Potter"
        actual_outcome = book_list.books[0].title
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_book_title2(self):
        expected_outcome = "No Plan B"
        actual_outcome = book_list.books[1].title
        self.assertEqual(expected_outcome, actual_outcome)
        
    def test_book_checkout(self):
        expected_outcome = False
        actual_outcome = book_list.books[0].check_out
        self.assertEqual(expected_outcome, actual_outcome)

    def test_book_checkout2(self):
        expected_outcome = False
        actual_outcome = book_list.books[1].check_out
        self.assertEqual(expected_outcome, actual_outcome)