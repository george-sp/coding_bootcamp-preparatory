# Write a program that asks the user the number of pronic numbers to output,
# then goes on and prints them.

# Prompt user for the number of pronic numbers and store the input as an int.
num_of_pronic_numbers = int(input("Enter number of pronic numbers: "))

# Print out the pronic numbers.
for n in range (1, num_of_pronic_numbers + 1):
    print(n * (n + 1), end=" ")
