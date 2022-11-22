# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_number = [number for number in numbers if number % 2 == 0]
print(even_number)

# 2. Print the difference between the largest and smallest value:
print(max(numbers) - min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.
for index in range(len(numbers)):
    if numbers[index] == 2 and numbers[index + 1] == 2:
        print(True)
    else:
        pass

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
sum = 0
skip = False
for number in numbers:
    if number == 6:
        skip = True
    if number == 7:
        skip = False
    elif skip == False:
        sum += number
print(sum)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
total = 0
for index in range(len(numbers)):
    if numbers[index] == 13:
        numbers[index] = 0
        numbers[index + 1] = 0
    else:
        total += numbers[index]
print(total)







