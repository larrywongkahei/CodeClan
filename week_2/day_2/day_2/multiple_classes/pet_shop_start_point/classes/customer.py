class Customer():
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.pet = []

    def reduce_cash(self, number):
        self.cash -= number

    def pet_count(self):
        return len(self.pet)

    def add_pet(self, pet):
        self.pet.append(pet)

    def get_total_value_of_pets(self):
        total = 0
        for i in self.pet:
            total += i.price
        return total

