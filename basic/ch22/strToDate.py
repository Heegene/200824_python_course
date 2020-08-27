# 날짜, 시간형식의 문자열을 datetime으로 만들 때도 strptime을 사용
import datetime

dayStr = '2019-11-23 12:11:32'
ThisdateTime = datetime.datetime.strptime(dayStr, '%Y-%m-%d %H:%M:%S')
# ThisdateTime = datetime.strptime(dayStr, '%Y-%m-%d %H:%M:%S')  --> 오류

print(type(ThisdateTime))  # [class 'datetime.datetime']
print('ThisdateTime->',ThisdateTime)  # 2018-07-28 12:11:32