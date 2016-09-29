"""
A program that asks the user to enter a sequence of digits
and then calculates the value of the sequence, as defined below:

- sequence: 1234567
- value: 1 * 2 + 3 * 4 + 5 * 6 + 7
"""

while True:
    num_sequence = input("Enter number sequence: ")
    try:
        int(num_sequence)
        break
    except ValueError:
        pass

sum = 0
for i in range (0, len(num_sequence), 2):
    if (i+1 < len(num_sequence)):
        sum += int(num_sequence[i]) * int(num_sequence[i+1])
    else:
        sum += int(num_sequence[i])
print(sum)
