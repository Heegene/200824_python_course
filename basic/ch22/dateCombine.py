# datetime.date와 datetime.time을 합치기 위해서는 datetime.datetime.combine을 이용
# 날짜만을 관리하기 위해서는 datetime.date, 시간만을 관리하기 위해서는 datetime.time
import datetime

d = datetime.date(2019, 11, 28)
t = datetime.time(12, 13, 18)

dt = datetime.datetime.combine(d, t)
print(dt)  # 2019-11-28 12:13:18