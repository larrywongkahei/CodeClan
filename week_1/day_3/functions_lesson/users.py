users = [
  { "user_id": 1, "first_name": "Guido", "last_name": "van Rossum" },
  { "user_id": 2, "first_name": "Katherine", "last_name": "Johnson" },
  { "user_id": 3, "first_name": "Dorothy", "last_name": "Vaughan" },
  { "user_id": 4, "first_name": "Hen", "last_name": "Solo" },
  { "user_id": 5, "first_name": "Mary", "last_name": "Jackson" },
]

def find_users(list, id):
    for user in list:
        if user["user_id"] == id:
            return user
    return None

desired_id = int(input("Please enter the desired user ID :"))
find_users_by_id = find_users(users, desired_id)
print(find_users_by_id)