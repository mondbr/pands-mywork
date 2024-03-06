# guess2.py
# the program tells the user if there guess is too high or too low
# each time they guess. HINT: put an if statement inside the while loop
# Author: Monika Dabrowska



number_to_guess = 30

guess = int(input("Please guess the number: "))
while guess != number_to_guess:
    if guess < number_to_guess:
        print ("too low")
    else:  # I know that can't be equal or too low, so it must be too high
        print ("too high")

    guess = int(input("Please guess again: "))

print ("Well done! Yes, the number was", number_to_guess)