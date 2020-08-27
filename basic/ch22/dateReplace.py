# 날짜나 시간을 변경하기 위해서는 replace 메서드를 사용
import datetime

myDatetime = datetime.datetime.strptime('2020-11-13 12:21:52', '%Y-%m-%d %H:%M:%S')
print(myDatetime)  # 2020-11-13 12:21:52

reDatetime = myDatetime.replace(day=27)
print(myDatetime)  # 2020-11-13 12:21:52
print(reDatetime)  # 2020-11-27 12:21:52

