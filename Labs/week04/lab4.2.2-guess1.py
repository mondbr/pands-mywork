# guess.py
# this program prompts the user to guess a number, 
# the program should keep prompting the user
# to guess the number until the user gets the right on

# author: Monika Dabrowska


number_to_guess = 30

guess = int(input("Please guess the number: "))
while guess != number_to_guess:
    print ("Wrong")
    guess = int(input("Please guess again: "))

print ("Well done! Yes, the number was {}".format (number_to_guess))
