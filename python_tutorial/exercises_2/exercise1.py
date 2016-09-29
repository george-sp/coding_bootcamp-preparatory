"""
A program that will ask the user for TIN and will respond whether it is correct or not.
"""

# Ask the user for TIN.
while True:
    tin = input('Enter Tax Identification Number: ')
    # Check if TIN has exact 9 digits.
    if (len(tin) == 9):
        break
    # If not, prompt the user again.
    else:
        print('The Greek Tax Identification Number(TIN) consists of 9 digits\n')


# Get the check digit.
check_digit = int(tin[-1])
# Add remove it from the tin.
rest_tin = tin[:len(tin) - 1]
# Reverse the tin.
reverse_rest_tin = rest_tin[::-1]

# Initialize a sum.
sum_powers = 0;
# Take the 8 digits one by one (from the right to the left == reverse_rest_tin).
for n in range(len(reverse_rest_tin)):
    # Increase the sum by the multiplication
    # of each digit by the power of 2 corresponding to its position.
    sum_powers += int(reverse_rest_tin[n]) * 2**(n+1)

# Calculate the remainder of the sum by 11.
remainder_1 = sum_powers % 11
# Calculate the remainder of the above remainder by 10.
remainder_2 = remainder_1 % 10

# Check if the result is equal to the check digit, and notify the user.
if (remainder_2 == check_digit):
    print("Tax Identification Number valid.")
else:
    print("Tax Identification Number not valid.")
