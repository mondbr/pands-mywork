# div.py
# this program reads in two numbers and
# outputs the integer answer and remainder

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y)      # "//" gives the divison
remainder = int(x%y)    # "%" gives the reminder

print ("{} divided by {} is {} with remainder {}" .format(x, y, answer, remainder))