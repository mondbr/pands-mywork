# sub.py

# this program reads in two numbers and subtracts the first from the second one. 
# input reads a string so we need to convert it into an int
# so we can perform mathematical operations

# author: Monika Dabrowska

x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))

# if we enter a string or float, it will cause an error

answer = int(x-y)

print("{} minus {} is {}".format(x, y, answer))

