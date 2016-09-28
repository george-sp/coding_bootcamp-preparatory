# Write a program that asks the user the number of triangular numbers to produce, and prints them out.

# Get input from user and store it as an int.
num_of_triangle_numbers = int(input("Enter number of triangle numbers: "))

# Print out the produced triangular numbers.
for n in range (1, num_of_triangle_numbers + 1):
    print((n * (n + 1)) // 2, end=" ")
