import datetime

d = datetime.date(2019, 11, 28)
t = datetime.time(12, 13, 18)

dt = datetime.datetime.combine(d,t)

print(dt) # 2019-11-28 12:13:18
