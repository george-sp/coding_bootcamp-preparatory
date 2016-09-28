# Write a program that calculates the first five terms of the harmonic sequence, that is, the numbers:
#             1
#           1 + 1/2
#       1 + 1/2 + 1/3
#   1 + 1/2 + 1/3 + 1/4
# 1 + 1/2 + 1/3 + 1/4 + 1/5

sum = 0

for i in range (1, 6):
    sum += 1/i
    print(sum)
