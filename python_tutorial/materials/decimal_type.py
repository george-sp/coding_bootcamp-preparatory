from decimal import Decimal

step = 0.1
total = 0
for i in range(1000):
    total += step
print(total)

# Python offers the Decimal type when we want exact arithmetic calculations.
step = Decimal(0.1)
total = 0
for i in range(1000):
    total += step
print(total)
