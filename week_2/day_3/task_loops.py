## Task one
ages = [5, 15, 64, 27, 84, 26]
list1 = [age for age in ages if age % 2 != 0]


## Task two
chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
list2 = [chicken for chicken in chicken_names if len(chicken) > 10]

list3 = [chicken for chicken in chicken_names if chicken.startswith("H")]

## Task three
words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
list4 = [letter[0].lower() for letter in words]

print(list1)
print(list2)
print(list3)
print(list4)