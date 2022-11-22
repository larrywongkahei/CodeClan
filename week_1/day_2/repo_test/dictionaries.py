meals = ('yoghurt', 'roll', 'steak')
print(meals[0])

my_first_empty_dictionary = {}
my_second_empty_dictionary = dict()

meals = {
    "breakfast" : "yoghurt",
    "lunch" : "roll", 
    "dinner" : "steak"
}
print(meals)

# Could be mixed with different type
things = {
    1 : "2", 
    "steve" : [1, 2, 3]
}

print("breakfast" in meals)

# To add an element in the dictionary
meals["supper"] = "pancakes"

# To delete an element in the dictionary
del(meals["breakfast"])
print(meals)

# To convert a dictionary to a list
list(meals)

# To print the keys
print(meals.keys())

# To print the values
print(meals.values())

# How to create dictionary inside a dictionary
countries = {
    "uk" : {"capital" : "London", "population" : 1000},
    "germany" : {"capital" : "Berlin", "population" : 5000},
}

print(countries["uk"]["population"])