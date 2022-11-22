class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.stock = {drink : 0 for drink in self.drinks }
    
    def increase_money(self, amount):
        self.till += amount

    def get_price_by_drink(self, drink):
        return drink.price

    def add_drink(self, drink):
        self.drinks.append(drink)
        if drink.name not in self.stock:
            self.stock[drink.name] = 1
        else:
            self.stock[drink.name] += 1

    def stock_value(self):
        total = 0
        for drink in self.drinks:
            total += drink.price * self.stock[drink.name]
        return total