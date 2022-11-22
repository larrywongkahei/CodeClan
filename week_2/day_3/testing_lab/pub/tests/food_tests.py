import unittest

from src.food import Food

class Testing(unittest.TestCase):
    def setUp(self):
        self.food = Food("Noodles", 20, 2)

    def test_food_has_name(self):
        self.assertEqual("Noodles", self.food.name)