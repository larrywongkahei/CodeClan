import unittest
from src.customer import Customer
from src.drinks import Drink
from src.pub import Pub
from src.food import Food

class Test_Customer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Larry", 500, 20)
    
    def test_customer_has_name(self):
        self.assertEqual("Larry", self.customer.name)

    def test_customer_cash(self):
        self.assertEqual(500, self.customer.wallet)

    def test_customer_could_afford(self):
        drink = Drink("Red bull", 20, 0)
        price = drink.price
        result = self.customer.can_afford(price)
        self.assertEqual(True, result)

    def test_customer_could_afford__NO(self):
        drink = Drink("GOLD WINE", 501, 2)
        price = drink.price
        result = self.customer.can_afford(price)
        self.assertEqual(False, result)

    def test_customer_age_enough(self):
        result = self.customer.age_enough()
        self.assertEqual(True, result)

    def test_customer_age_enough__NO(self):
        new_customer = Customer("Tim", 20, 17)
        result = new_customer.age_enough()
        self.assertEqual(False, result)

    def test_customer_able_to_buy_drink(self):
        self.pub = Pub("Larry's", 1000)
        drink = Drink("Red bull", 20, 0)
        self.customer.buy_drink(self.pub, drink)
        self.assertEqual(1020, self.pub.till)
        self.assertEqual(480, self.customer.wallet)

    def test_customer_able_to_buy_drink__NOT_AGE_ENOUGH(self):
        self.pub = Pub("Larry's", 1000)
        drink = Drink("Red bull", 20, 0)
        new_customer = Customer("Tim", 500, 17)
        new_customer.buy_drink(self.pub, drink)
        self.assertEqual(1000, self.pub.till)
        self.assertEqual(500, self.customer.wallet)

    def test_customer_able_to_buy_drink__CANT_AFFORD(self):
        self.pub = Pub("Larry's", 1000)
        drink = Drink("Red bull", 20, 0)
        new_customer = Customer("Tim", 10, 25)
        new_customer.buy_drink(self.pub, drink)
        self.assertEqual(1000, self.pub.till)
        self.assertEqual(500, self.customer.wallet)

    def test_customer_able_to_buy_drink__DRUNK(self):
        self.pub = Pub("Larry's", 1000)
        drink = Drink("Red bull", 20, 0)
        new_customer = Customer("Tim", 500, 25)
        new_customer.drunkenness_level = 5
        new_customer.buy_drink(self.pub, drink)
        self.assertEqual(1000, self.pub.till)
        self.assertEqual(500, self.customer.wallet)

    def test_customer_drunkenness_level(self):
        result = self.customer.drunkenness_level
        self.assertEqual(0, result)

        self.pub = Pub("Larry's", 1000)
        drink = Drink("GOLD WINE", 501, 2)
        self.customer.buy_drink(self.pub, drink)
        new_result = self.customer.drunkenness_level
        self.assertEqual(2, new_result)
         
        food = Food("Noodles", 10, 2)
        level = food.rejuvenation_level
        self.customer.ordered_food(level)
        last_result = self.customer.drunkenness_level
        self.assertEqual(0, last_result)

    