# convert.py
# this program takes in a float amount of dollars and returns that absolute amount in cent
# author: Monika Dabrowska


# Taking input from the user
input_amount = float(input("Please enter an amount: "))


# Converting to cents and displaying the result
cents = abs(int(input_amount * 100))

# Display the result
print(f"that amount in cent is: {cents} cents")
