# round.py
# this program should take in a float and output an int
# be careful of round, it rounds to the nearest even number
# eg 4.5 rounds to 4
# so do not use it accuracy is essential
# author: Monika Dabrowska

number_to_round = float(input("Enter a float number: "))
rounded_number = round(number_to_round)
print ("{} rounded is {}" .format (number_to_round, rounded_number))
