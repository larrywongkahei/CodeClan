def compare(user_number, computer_number):
    if user_number > computer_number:
        return f"{user_number} is greater than my number"
    elif user_number < computer_number:
        return f"{user_number} is less than my number"
    else:
        return "Bingo!Congrat!"