from dateutil.relativedelta import relativedelta
from datetime import datetime
import time

t1 = time.time()
t2 = time.localtime(t1)
t3 = time.asctime(t2)

print(t1)
print(t2)
print(t2.tm_year)
print(t3)

############################

dt1 = datetime.now()
print(f"Datetime 1: {dt1}")
print(f"Datetime 1: {dt1.date()}")

print("Hour:", str(dt1.hour).zfill(2))
print("Minute:", f"{dt1.minute:02d}")
print("Second:", f"{dt1.second:02d}")
# print("Second:",f"{a:<02d}".format(a=dt1.second)) # proof i'm not ok lol
print("Second: {a:>02d}".format(a=dt1.second))
print("Second:", format(dt1.second, '02d'))

""" 
    print(f"Datetime 1: {dt1}".format(dt1=dt1.date())) # doesn't work
    print(f"Datetime 1: {dt1}".format(dt1=dt1.date())) # doesn't work
    print(f"Datetime 1: {a}".format(a=dt1.date())) # doesn't work
    print("Datetime 1: {a}".format(a=dt1.date())) # does work (freaking literals)
    
"""

########################

dt2 = datetime.now().date()
print(f"Date 2: {dt2}")

print(f"Day: {dt2.day}")
print(f"Month: {dt2.month}")
print(f"Year: {dt2.year}")

################################

strDate = input("Insert your date of birth: ")
dt3 = datetime.strptime(strDate, "%d-%m-%Y").date()

print(f"Your date of birth is on {dt3}")

"""

# match

def suffix(day):
    default = "th"

    switcher = {
        "1": "st",
        "2": "nd",
        "3": "rd"
    }

    return switcher.get(str(day)[-1], default)

"""


print(f"Your age is {(dt2-dt3)}")

print(f"Your age is {(dt2.year-dt3.year)}")

#######################################


difference_in_years = relativedelta(dt2, dt3).years

print(difference_in_years)
