"""
Asks the user to enter two dates in the form dd/mm/yyyy
and will then display the number of days that have elapsed between the two days.

To calculate the number of days between two days we can use the following algorithm.
Let's say that the first date is given by y1, m1, d1 and the second date is given by y2, m2, d2.

1. c1 = |(306m1 + 5)/10| + (d1-1)
2. c2 = |(306m2 + 5)/10| + (d2-1)
3. |c2-c1|

* The two dates must be support from the datetime format.
  No negative yyyy is supported.
"""

import datetime

def checkDateFormat(num_of_dates=2):
    for i in range (2):
        try:
            dates[i] = datetime.datetime.strptime(dates[i], '%d/%m/%Y')
        except ValueError:
            return False
    return True

while True:
    dates = input('Enter dates: ').split(" ")
    if (len(dates) == 2):
        if (checkDateFormat()):
            break
        else:
            print("Incorrect date format!",
                  "Enter two dates in the form dd/mm/yyyy.\n")
    else:
        print("Give two dates..\n")

# c1 = 365y1 + |y1/4| − |y1/100| + |y1/400| + |(306m1 + 5)/10| + (d1-1)
c1 = 365*dates[0].year + dates[0].year//4 - dates[0].year//100 + dates[0].year//400
c1 += (306*dates[0].month + 5)//10 + (dates[0].day - 1)
# c2 = 365y2 + |y2/4| − |y2/100| + |y2/400| + |(306m2 + 5)/10| + (d2-1)
c2 = 365*dates[1].year + dates[1].year//4 - dates[1].year//100 + dates[1].year//400
c2 += (306*dates[1].month + 5)//10 + (dates[1].day - 1)
# |c2 - c1|
if (c2 > c1):
    print(c2 - c1)
else:
    print(c1 - c2)
