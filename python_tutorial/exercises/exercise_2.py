# Write a program that asks the user to provide different numbers of banknotes and coins, from €50 to €1. 
# Then output the total sum in euros.

# Initialize the sum and assign 0 to it.
sum = 0;

# Ask user for different numbers of banknotes and coins.
user_input = input("Enter number of 50 euro banknotes: ")
# Increase the sum.
sum += int(user_input) * 50
user_input = input("Enter number of 20 euro banknotes: ")
sum += int(user_input) * 20
user_input = input("Enter number of 10 euro banknotes: ")
sum += int(user_input) * 10
user_input = input("Enter number of 5 euro banknotes: ")
sum += int(user_input) * 5
user_input = input("Enter number of 2 euro coins: ")
sum += int(user_input) * 2
user_input = input("Enter number of 1 euro coins: ")
sum += int(user_input) * 1

# Print the sum.
print("You have", sum, "euros")
