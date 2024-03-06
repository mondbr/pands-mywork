# absolute.py
# this program takes in number and give its absolute value

# author: Monika Dabrowska

# In the question, number is ambiguous, but
# the output implies that we should be dealing with floats
# I need to change the input to float

number = float(input("Enter a number"))
absolute_value = abs(number)

print("The absolute value of {} is {}" . format(number, absolute_value))
