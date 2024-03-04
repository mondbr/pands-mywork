# grade.py
# this program reads in a student's percentage mark and 
# prints out out corresponding the grade
# the program should check that the percentage is valid

# Author: Monika Dabrowska

# print the percentage:
percentage = float(input("Enter the percentage: "))

# be careful with ands and ors
if percentage <0 or percentage >100:
        # error handling - to be clarified later
        # This should really throw an error

    print(f"Please enter a number between 0 and 100")
elif percentage < 40: # we know that is greater than 0
    print (f"Fail")
elif percentage < 50: # between 40 and 49
    print (f"Pass")
elif percentage < 60: # between 50 and 59
    print (f"Merit1")
elif percentage < 70: # between 60 and 69
    print (f"Merit2")
else: # the only option left is between 70 and 100
    print (f"Distinction")
