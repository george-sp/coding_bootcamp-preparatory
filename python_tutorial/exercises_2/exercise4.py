"""
A program that asks the user for a 9-digit number
and then prints it in three lines.

Each line must contain three digits.
Each number must be in a column by itself.
"""

# Ask the user for a 9-digit number.
while True:
    user_input = input("Enter 9 digit number: ")
    if (len(user_input) == 9):
        break
    else:
        print(int(len(user_input)), 'digits. This is not a 9 digit number.\n')

# Prepare the strings for each line. Take care of the indentation.
line_1 = ""
line_2 = " "
line_3 = "  "

# Set up a counter so that can move between lines.
counter = 1
for i in range(9):
    if (counter == 1):
        line_1 += " " + user_input[i] + " "
    elif (counter == 2):
        line_2 += " " + user_input[i] + " "
    elif (counter == 3):
        line_3 += " " + user_input[i] + " "

    # Increase the counter by 1.
    counter += 1
    # There is not a line 4 so reset the counter to 1.
    if (counter == 4):
        counter = 1

# Print the lined up numbers.
print(line_1)
print(line_2)
print(line_3)
