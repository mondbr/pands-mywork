# average.py
# that keeps reading numbers until the user enters a 0
# program should then print out each of the numbers entered and the average of them. (Using list)

# author: Monika Dabrowska



numbers = []

# enter first number then check if it is 0 in the while loop

number = int(input("Enter number (0 to quit): "))
while number !=0:
    numbers.append(number)

    # read the text number and check if 0
    number = int((input)("Enter another number (0 to quit): "))

for value in numbers:
    print (value)

# I want to average to be a float:
average = float(sum(numbers)) / len(numbers)
print (f'The average is {average}')

