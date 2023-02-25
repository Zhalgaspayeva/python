import datetime

x3 = datetime.datetime.now()
year = int(input())
month = int(input())
day = int(input())

if (x3.year != year):
    year_time = ((x3.year - year) * 365 * 24 * 60)
elif (x3.year == year):
    year_time = 0

if (x3.month != month):
    month_time = ((x3.month - month) * 30 * 24 * 60)
elif (x3.month == month):
    month_time = 0

if (x3.day != day):
    day_time = ((x3.day - day) * 24 * 60)
elif (x3.day == day):
    day_time = 0

calc = ((day_time + month_time + year_time) * 60) + x3.minute * 60
print(calc)