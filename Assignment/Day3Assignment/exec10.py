# day of given date

from datetime import date
day,month,year =list(map(int,input("enter date(eg: 01 02 2000):").split()))
print(day,month,year)
day_name = date(year,month, day)
print(day_name.strftime("%A"))