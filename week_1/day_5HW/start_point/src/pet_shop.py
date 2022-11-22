# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

# Add the certain number in cash
def add_or_remove_cash(shop, number):
    shop["admin"]["total_cash"] += number

# Remove the certain number in cash
def add_or_remove_cash_add_remove(shop, number):
    shop["admin"]["total_cash"] -= number

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

# Add the certain number in the pets sold number
def increase_pets_sold(shop, number):
    shop["admin"]["pets_sold"] += number


def get_stock_count(shop):
    return len(shop["pets"])


# Create a for loop in shop["pets"],
# To check whether whre shop["pets"]["breed"] is equal to the breed.
# Return how many in the list.
def get_pets_by_breed(shop, breed):
    return [name for name in shop["pets"] if name["breed"] == breed]
    # empty_list = []
    # for name in shop["pets"]:
    #     if name["breed"] == breed:
    #         empty_list.append(name)
    # return empty_list

def find_pet_by_name(shop, name):
    # return (pet for pet in shop["pets"] if shop["pets"]["name"] == name)
    for pet in shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            shop["pets"].remove(pet)

def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, number):
    customer["cash"] -= number

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    return True if customer["cash"] >= new_pet["price"] else False

def sell_pet_to_customer(shop, pet, customer):
    if pet and customer_can_afford_pet(customer, pet):
        increase_pets_sold(shop, 1)
        remove_customer_cash(customer, pet["price"])
        add_pet_to_customer(customer, pet)
        add_or_remove_cash(shop, pet["price"])
    else:
        pass
