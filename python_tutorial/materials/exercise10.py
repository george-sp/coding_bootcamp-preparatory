"""
Ask the user to enter a sequence of 0s and 1s.
Identify the longest run of 0s or 1s of the sequence and print an appropriate message.
"""

# Prompt user a binary sequence.
while True:
    binary_sequence = input("Enter binary sequence: ")
    num_of_zeros = binary_sequence.count('0')
    num_of_ones = binary_sequence.count('1')
    sequence_size = len(binary_sequence)
    # Check if it is a valid binary sequence.
    if (num_of_ones + num_of_zeros == sequence_size):
        break

# Set up some helper variables and "longest run" counters.
previous_digit = binary_sequence[0]
length_0s = 0
length_1s = 0
sum_0s = [0]
sum_1s = [0]

# Iterate the given binary sequence.
for digit in binary_sequence:
    # Check if the current digit is the same as the last one.
    if (digit == previous_digit):
        # If it is, increase the appropriate run.
        if (previous_digit == '0'):
            length_0s += 1
        else:
            length_1s += 1
    # If the previous digit is different from this one.
    else:
        # Save the run and start again.
        if (previous_digit == '0'):
            sum_0s.append(length_0s)
            length_0s = 0
            length_1s = 1
        else:
            sum_1s.append(length_1s)
            length_1s = 0
            length_0s = 1
    previous_digit = digit

# Add the current runs to the sum lists.
sum_0s.append(length_0s)
sum_1s.append(length_1s)

# Get the longest run of each digit.
length_0s = max(sum_0s)
length_1s = max(sum_1s)

# Print the appropriate message.
if (length_0s > length_1s):
    print("Longest run was zeros with length:", length_0s)
elif (length_0s < length_1s):
    print("Longest run was ones with length:", length_1s)
else:
    print("Equal longest run of ones and zeros with length: ", length_0s)
