# Define a non-empty tuple
car = ('Ford', 'Escort', 1300, 'Red')
car_2 = 'Ford', 'Escort', 1300, 'Red'
print(car)
print(type(car))
print(car_2)
print(type(car_2))

# Define an empty tuple
empty_tumple = ()
empty_tumple2 = tuple()
print(empty_tumple)
print(type(empty_tumple))
print(empty_tumple2)
print(type(empty_tumple2))

# Access value by index
model = car[1]
colour = car[-1]
print(f'Model: {model} colour: {colour}')

# Can't modify though!
# car[1] = 'Focus'

# Count tuple elements
tuple_count = len(car)
print(tuple_count)

# Using the count method
fruits = ('apple', 'apple', 'banana')
print(fruits.count('apple'))

# Tuple of a single element
single_tuple = ('ben')
print(type(single_tuple))
