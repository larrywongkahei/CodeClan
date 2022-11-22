users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

########

# Not sure if get is to print out
# So I create a variable for them

 ########
# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
Jonathan_Twit_handle = users["Jonathan"]["twitter"]
print(Jonathan_Twit_handle)

# 2. Get Erik's hometown
Erik_hometown = users["Erik"]["home_town"]
print(Erik_hometown)

# 3. Get the list of Erik's lottery numbers
Erik_lottery_nums = users["Erik"]["lottery_numbers"]
print(Erik_lottery_nums)

# 4. Get the species of Avril's pet Monty
Avril_pet_species = users["Avril"]["pets"][0]["species"]
print(Avril_pet_species)

# 5. Get the smallest of Erik's lottery numbers
Erik_smallest_lottery = min(Erik_lottery_nums)
print(Erik_smallest_lottery)

# 6. Return an list of Avril's lottery numbers that are even
Even_numbers = [number for number in users["Avril"]["lottery_numbers"] if number % 2 == 0 ]
print(Even_numbers)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
Erik_lottery_nums.append(7)
print(Erik_lottery_nums)

# 8. Change Erik's hometown to Edinburgh
Erik_hometown = "Edinburgh"
print(Erik_hometown)

# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append({"name": "fluffy", "species": "dog"})
print(users["Erik"]["pets"])

# 10. Add another person to the users dictionary
users["Larry"] = {
  "twitter": "Larrywong",
  "lottery_numbers": [1, 2, 3, 4, 5, 6],
  "home_town": "HongKong",
  "pets": [
    {
      "name": "SaSa",
      "species": "dog"
    },
    {
      "name": "Candy",
      "species": "dog", 
    }
  ]
}