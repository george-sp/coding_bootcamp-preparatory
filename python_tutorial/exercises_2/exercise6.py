"""
Ask the user for 9 numbers:
- 1 with 1 digit, 1 with 2 digits, 1 with 3 digits
- 1 with 1 digit, 1 with 2 digits, 1 with 3 digits
- 1 with 1 digit, 1 with 2 digits, 1 with 3 digits.

Then the program will print them in columns,
where each column will contain:
- 1 single digit number
- 1 double digit number
- 1 triple digit number.

The columns will be 3 characters wide and
will be separated from each other with the character |.

The numbers inside the columns will be right justified.
"""

example = 'Example: 1 10 100 2 20 200 3 30 300\n'
user_input = []

# Checks the number of digits according to: 1 digit, 2 digits, 3 digits repeats.
# Returns True if the repeats are correct.
def checkDigits(num_list):
    for i in range (3):
        appropriate_length = i + 1
        if (len(num_list[i]) != appropriate_length or
            len(num_list[i + 3]) != appropriate_length or
            len(num_list[i + 6]) != appropriate_length):
            return False;
    return True;

# Returns a formatted string.
def formatColumns(num_list):
    formatted_string = ""
    line_1 = ""
    line_2 = ""
    line_3 = ""
    for i in range (9):
        if (len(num_list[i]) == 1):
            line_1 += 2*" " + num_list[i] + "|"
            continue
        if (len(num_list[i]) == 2):
            line_2 += " " + num_list[i] + "|"
            continue
        if (len(num_list[i]) == 3):
            line_3 += num_list[i] + "|"
    # print(line_1, line_2, line_3)
    formatted_string = line_1[:-1] + "\n" + line_2[:-1] + "\n" + line_3[:-1]
    return formatted_string

# Take 9 numbers from the user
while True:
    # Ask user's input and store it a list.
    user_input = input('Enter numbers: ').split(' ')
    # Check if there are 9 numbers.
    if (len(user_input) != 9):
        print(example)
    else:
        # If there are, check for the 1,2,3 digits repeat.
        if (checkDigits(user_input)):
            break
        else:
            print(example)

print(formatColumns(user_input))
