# extra.py
# program generates a random number between 0 and 100 to guess 
# author: Monika Dabrowska



import random

number_to_guess = random.randint(0,100)

guess = int(input("Please guess the number: "))
while guess != number_to_guess:
    print ("Wrong")
    guess = int(input("Please guess again: "))

print ("Well done! Yes, the number was {}".format (number_to_guess))

