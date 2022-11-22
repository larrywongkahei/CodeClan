import unittest
from src.pub import Pub
from src.drinks import Drink

class Test_Pub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Larry's", 1000)

    def test_pub_has_name(self):
        self.assertEqual("Larry's", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(1000, self.pub.till)

    def test_add_drink(self):
        drink1 = Drink("Red bull", 20, 0)
        drink2 = Drink("Monster", 15, 0)
        drink3 = Drink("Black label", 50, 3)
        self.pub.add_drink(drink1)
        self.pub.add_drink(drink2)
        self.pub.add_drink(drink3)
        self.assertEqual("Red bull", self.pub.drinks[0].name)
        self.assertEqual("Monster", self.pub.drinks[1].name)
        self.assertEqual("Black label", self.pub.drinks[2].name)
    

    