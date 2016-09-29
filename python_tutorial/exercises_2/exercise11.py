"""
The program asks the user for an upper limit and then prints out the polite
up to and including the limit.
The program should not use logarithms.
The numbers should be written in rows of 10 (except possibly for the last line).
- The positive integer numbers that can be written as the sum of two or more
  consecutive positive integers are called polite numbers.
- The rest are called impolite numbers.
- It can be proven that the impolite numbers are the powers of 2.
- The first polite numbers are:
  3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21,
  22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37,
  38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, ...
"""

# Get the upper limit from the user.
while True:
    try:
        # Check that user input is a number.
        upper_limit = int(input("Enter limit: "))
        break
    except ValueError:
        pass

# Declare a list, to store the powers of 2.
powers_of_two = []

# Get the powers of 2 that are smaller or equal to the limit.
counter = 1
while True:
    if (2**counter <= upper_limit):
        powers_of_two.append(2**counter)
    else:
        break
    counter += 1

# Start to count from 3 to the upper limit.
counter = 0
for i in range(3, upper_limit + 1):
    # Print all the numbers except for the powers of 2.
    if i not in powers_of_two:
        print(i, end=" ")
        counter = counter + 1 if counter < 9 else 0
    # Print 10 numbers in each line.
    if (counter == 0):
        print()
