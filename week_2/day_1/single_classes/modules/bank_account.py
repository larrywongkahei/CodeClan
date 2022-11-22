# def get_account_name(list):
#     return list["holder_name"]

class BankAccount:
    def __init__(self, holder_name, balance, type):
        self.name = holder_name
        self.balance = balance
        self.type = type
        self._rates = {
            "personal": 10,
            "business": 50,
        }

    def pay_in(self, amount):
        self.balance += amount
    
    def pay_monthly_fee(self):
        self.balance -= self._rates[self.type]
