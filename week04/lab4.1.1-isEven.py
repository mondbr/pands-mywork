# isEven.py
# this program asks the user to enter in a number, 
# and the program will tell the user if the number is even or odd
# 
# author: Monika Dabrowska

number = int(input("Enter an integer: "))

# remainder of number divided by 2 must be 0
if (number % 2) == 0:
    # if it is true
    print (f"{number} is an even number")


    # if not:
else: 
    print (f"{number} is an odd number")