# # def greet(name, time_of_day):
# #     return "Good" + time_of_day + "," + name

# # name_1 = "Ash"
# # time_of_day_1 = "Morning"
# # greeting = greet(name_1, time_of_day_1)
# # print(greeting)

# # name_1 = "Ben"
# # time_of_day_1 = "Afternoon"
# # greeting = greet(name_1, time_of_day_1)
# # print(greeting)

# def greet():
#     words = "Hey"
#     return words

# def greet_Two():
#     words = "Hey"
#     return words
# print(greet_Two())

chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

# def count_eggs(list):

#     total_eggs = 0

#     for chicken in chickens:
#         total_eggs += chicken["eggs"]
#         chicken["eggs"] = 0 # eggs have been collected

#     print(f"{total_eggs} eggs collected")
# count_eggs(chickens)

def find_chicken_by_name(list, name):
    for chicken in chickens:
        if chicken["name"] == name:
            return chicken
chicken = find_chicken_by_name(chickens, "Margaret")
print(chicken)
