import unittest
from src.drinks import Drink

class Test_Pub(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Red bull", 20)

    def test_drinks_has_name(self):
        self.assertEqual("Red bull", self.drink.name)

    def test_drinks_price(self):
        self.assertEqual(20, self.drink.price)