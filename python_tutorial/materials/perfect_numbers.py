# A perfect number is a number that is the sum of all its divisors, except for itself.
# We do not currently know whether there are infinitely many perfect numbers.
# Perfect numbers appear as early as as early Euclid's Elements (VII.22).

for test_number in range(1, 10000):
    sum = 0
    for i in range(1, test_number):
        if test_number % i == 0:
            sum += i
    if sum == test_number:
        print(test_number, "is a perfect number")
