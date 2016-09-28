# Write a program that asks the user for the three sides of a triangle
# and calculates its area.

import math

# Get the vales from the user.
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

# Calculate the area of the triangle.
area_A = 1/4 * math.sqrt((a+b+c) * (-a+b+c) * (a-b+c) * (a+b-c))

# And print it.
print(area_A)
