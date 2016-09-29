"""
A program that asks the user for a 10-digit number
and will then print it in two lines.

The first line will contain the numbers in the odd positions
and the second the numbers in the even positions.

Each number must be in a column by itself.
"""

# Ask the user for a 10 difit number.
while True:
    user_input = input("Enter 10 digit number: ")
    if (len(user_input) != 10):
        print(int(len(user_input)), 'digits. This is not a 10 digit number.\n')
        continue
    else:
        break

# Initialize two empty strings, one per line.
odd_position_nums = ''
even_position_nums = ''

# Iterate the 10-digit number.
for i in range (10):
    if (i % 2 == 0):
        # Add the numbers in even position.
        even_position_nums += user_input[i] + " "
    else:
        # Add the numbers in odd position.
        odd_position_nums += " " + user_input[i]

# Print the two lines of numbers.
print(even_position_nums)
print(odd_position_nums)
