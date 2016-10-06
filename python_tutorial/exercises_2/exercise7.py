"""
Asks the user to enter two dates in the form dd/mm/yyyy
and will then display the number of days that have elapsed between the two days.

To calculate the number of days between two days we can use the following algorithm.
Let's say that the first date is given by y1, m1, d1 and the second date is given by y2, m2, d2.

1. c1 = 365y1 + ⌊y1/4⌋ − ⌊y1/100⌋ + ⌊y1/400⌋ + ⌊(306m1 + 5)/10⌋ + (d1−1)
2. c2 = 365y2 + ⌊y2/4⌋ − ⌊y2/100⌋ + ⌊y2/400⌋ + ⌊(306m2 + 5)/10⌋ + (d2−1)
3. c2-c1
"""

dates = input('Enter dates: ').split(" ")

date_1 = dates[0].split("/")
date_2 = dates[1].split("/")

for i in range(3):
    date_1[i] = int(date_1[i])
    date_2[i] = int(date_2[i])

# c1 = 365y1 + ⌊y1/4⌋ − ⌊y1/100⌋ + ⌊y1/400⌋ + ⌊(306m1+5)/10⌋ + (d1−1)
c1 = 365*date_1[2] + date_1[2]//4 - date_1[2]//100 + date_1[2]//400 + (306*date_1[1] + 5)//10 + (date_1[0] - 1)
# c2 = 365y2 + ⌊y2/4⌋ − ⌊y2/100⌋ + ⌊y2/400⌋ + ⌊(306m2+5)/10⌋ + (d2−1)
c2 = 365*date_2[2] + date_2[2]//4 - date_2[2]//100 + date_2[2]//400 + (306*date_2[1] + 5)//10 + (date_2[0] - 1)
# c2 - c1
if (c2 > c1):
    print(c2 - c1)
else:
    print(c1 - c2)
