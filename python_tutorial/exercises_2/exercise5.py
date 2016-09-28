"""
This program asks the user for a year and then displays
the month and the year of Orthodox Easter in the Gregorian calendar.

The follow algorith can be used to calculate the Orthodox Easter Sunday
for any year between 1900 and 2099.
(Suppose that y is the year)
1. a = y mod 4
2. b = y mod 7
3. c = y mod 19
4. d = (19c + 15) mod 30
5. e = (2a + 4b - d + 34) mod 7
6. month = |((d + e + 114) / 31)| , |x| means the integer part of x
                                    that is, x round down towards 0.
7. day = ((d + e + 114) mod 31) + 1
8. The result is the day and the month in the Julian Calendar.
   to convert it to the Gregorian calendar, add 13 days.
"""

import math
import datetime

while True:
    y = int(input("Enter year: "))
    if (y >= 1900 and y <= 2099):
        break
    else:
        print('To calculate the Orthodox Easter Sunday\nuse any year between 1900 and 2099 not,', y, '.\n')

# Run the given algorithm.
a = y % 4
b = y % 7
c = y % 19
d = (19 * c + 15) % 30
e = (2*a + 4*b - d + 34) % 7
month = math.floor((d + e + 114) / 31)
day = ((d + e + 114) % 31) + 1

easter = datetime.date(int(y), int(month), int(day)) + datetime.timedelta(days=13)
print('Day: ', easter.day, 'Month: ', easter.month)
# 2011 (24,4), 2012 (15/4), 2013 (5/5), 2014 (20/4), 2015 (12/4), 2016 (1/5), 2017 (16/4).
