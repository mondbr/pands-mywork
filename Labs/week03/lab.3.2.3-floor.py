# floor.py
# this program takes a float and outputs an int rounded down

# author: Monika Dabrowska




import math

number_to_floor = float(input("Enter a float number: "))

# Use math.foor() to round down the float to the nearest integer
floored_number = (math.floor(abs(number_to_floor))) #abs is added to take absolute number


# Prints the result
print("{} floored is {}" .format((number_to_floor), floored_number))


