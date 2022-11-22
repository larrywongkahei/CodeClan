import unittest
from modules.cat import *
class TestCats(unittest.TestCase):
    def test_something(self):
        cat = Cat()
        result = cat.greeting()
        self.assertEqual("hi", result)