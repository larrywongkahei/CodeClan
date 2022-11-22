def return_10():
    return 10

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def length_of_string(string):
    return len(string)

def join_string(str1, str2):
    return str1 + str2

def add_string_as_number(str1, str2):
    return int(str1) + int(str2)

def number_to_full_month_name(number):
    months = {
        1 : "January", 
        2 : "February",
        3 : "March",
        4 : "April", 
        5 : "May",
        6 : "June",
        7 : "July",
        8 : "August", 
        9 : "September",
        10 : "October",
        11 : "November",
        12 : "December",
    }
    return months[number]

def number_to_short_month_name(number):
    months = {
        1 : "Jan", 
        2 : "Feb",
        3 : "Mar",
        4 : "Apr", 
        5 : "May",
        6 : "Jun",
        7 : "July",
        8 : "Aug", 
        9 : "Sep",
        10 : "Oct",
        11 : "Nov",
        12 : "Dec",
    }
    return months[number]

###         Further ####
def volume_of_cube(length):
    return length ** 3

def reverse_string(string):
    return string[::-1]

def fahrenheit_to_celsius(fahrenheit_temp):
    return round((fahrenheit_temp - 32) * 5 / 9, 2)