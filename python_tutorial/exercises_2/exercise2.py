"""
This is program that asks the user for an 8-bit binary number
and replies whether the parity bit checks OK.

Parity bits are used as the simplest form of error detecting code.
"""

# Get a byte from the user.
while True:
    bits_8 = input("Enter binary number: ")
    # Check if user inserted 8 bits.
    if (len(bits_8) == 8):
        break
    # If not, prompt the user again.
    else:
        print('A byte consists of 8 bits. Try again.\n')

# Get the last bit.
last_bit = int(bits_8[-1])
# Seperate the first 7 bits.
bits_7 = bits_8[:7]

# The sum of 1 bits.
sum_of_ones = 0;
for bit in bits_7:
    if (int(bit) == 1):
        sum_of_ones += 1

if (sum_of_ones % 2 != 0 and last_bit == 1):
    print("Parity check OK.")
else:
    print("Parity check not OK.")
