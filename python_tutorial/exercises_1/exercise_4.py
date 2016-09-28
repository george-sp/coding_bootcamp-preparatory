# Write a program that asks the user to enter values for a, b, c,
# then prints the solutions of the quadratic equation they define, if they exist.
# If they do not exist, it should ou

import math

# Get values a, b, c from user.
a = int(input("Give a value to a: "))
b = int(input("Give a value to b: "))
c = int(input("Give a value to c: "))

# Check for no real-valued solutions.
if (b**2 - 4*a*c < 0):
    print("No real-valued solutions exist")
else:
    root_1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    root_2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    print("The solutions are: root_1 =", root_1, "and root_2", root_2)
