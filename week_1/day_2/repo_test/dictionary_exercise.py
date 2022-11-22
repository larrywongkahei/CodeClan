# Setting up avengers' name and skills
avengers = {
    "Iron Man": {
        "Name": "Tony Stark", 
        "Attack": {
            "punch": 10, 
            "kick": 100
        }
    },
    "Hulk": {
        "Name": "Bruce Banner", 
        "Attack": {
            "smash": 1000, 
            "roll": 500
        }
    }
}

# Print out the certain avengers' skill's damage
print(avengers["Hulk"]["Attack"]["smash"])