# SET is_it_raining = INPUT" is it raining?"
# IF is_it_raining is "yes" and distance < 5:
# Print "You should take the car"
# ELSE 
#  IF distance < 5:


# To make it all lower.
# is_it_raining = input("Is it raining?").lower()

# if is_it_raining == "yes":
#     print("You should take the car")
# else:
#     if distance < 5:
#         print("You should walk")
#     else:
#         print("You should get the bus")

# To avoid error if accidentally tap SPACE
# if "yes" in is_it_raining:
#     print("You should take the car")

# MY VERSION
is_it_raining = input("Is it raining?").lower()
if is_it_raining == "yes":
    print("You should take the bus")
elif is_it_raining == "no":
    distance = int(input("How far is the destination?"))
    if distance < 5:
        print("You should walk")
    else:
        print("You should take the bus")
