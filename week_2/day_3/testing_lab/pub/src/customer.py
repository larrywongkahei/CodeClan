class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness_level = 0

    def deduct_cash(self, price):
        self.wallet -= price

    def buy_drink(self, pub, drink):
        price = pub.get_price_by_drink(drink)
        alcohol_level = drink.alcohol_level
        self.add_drunkenness(alcohol_level)
        if self.can_afford(price) and self.age_enough() and self.drunkenness_level <= 3:
            self.deduct_cash(price)
            pub.increase_money(price)

    def can_afford(self, price):
        return self.wallet >= price
    
    def age_enough(self):
        return self.age >= 18

    def add_drunkenness(self, alcohol_level):
        self.drunkenness_level += alcohol_level

    def ordered_food(self, level):
        if level > self.drunkenness_level:
            self.drunkenness_level = 0
        else:
            self.drunkenness_level -= level

    


    