from datetime import date, timedelta
sdate = date(2020, 12, 31)   # start date
edate = date(2021, 4,30)   # end date

delta = edate - sdate       # as timedelta

for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    print(day)
