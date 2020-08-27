import datetime

myDatetime = datetime.datetime.strptime('2020-11-13 12:21:52', '%Y-%m-%d %H:%M:%S')
print(myDatetime) # 2020-11-13 12:21:52

reDateTime = myDatetime.replace(day=27)
print(myDatetime)
print(reDateTime) # 2020-11-27 12:21:52
