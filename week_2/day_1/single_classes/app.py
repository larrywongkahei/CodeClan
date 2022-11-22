from modules.bank_account import *
account = {
    "holder_name": "John",
    "balance": 500,
    "type": "business"
}
account_1 = BankAccount("John", 500, "business")
print(account_1.name)
print(account_1.balance)
account_1.pay_in(20)
print(account_1.balance)
account_1.pay_monthly_fee()
print(account_1.balance)

account_2 = BankAccount("Larry", 1000, "personal")
print(account_2.balance)
account_2.pay_monthly_fee()
print(account_2.balance)