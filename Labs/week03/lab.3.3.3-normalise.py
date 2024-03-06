# This program reads in a string and strips
# any leading of trailing spaces.
# It also converts all the letters to lower case.
# It then outputs the lengths of the original string
# and the normalised one
#
# Author: Monika Dabrowska

# ask the user to enter a string
raw_string = input("Please enter a string: ")

# correcting the string with removing whitespaces "strip()" and converts a string into lower case "lower()"
normalised_string = raw_string.strip().lower()

# checking the lenght of the string before and after corrections
lenght_of_raw_string = len(raw_string)
lenght_of_normalised = len(normalised_string)

print("That String normalised is {}:".format(normalised_string))
print("we reduced the input string from {} to {}" .format(lenght_of_raw_string, lenght_of_normalised))

