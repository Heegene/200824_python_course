import datetime

now = datetime.datetime.now()
print(now)  # Current Date Time

# 시간을 문자열로 출력하려면 strftime 메서드를 사용
nowDate = now.strftime('%Y-%m-%d')
print(nowDate)  # Current Date

nowTime = now.strftime('%H:%M:%S')
print(nowTime)  # Current Time

# 시간을 문자열로 출력하려면 strftime 메서드를 사용
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)  # Current Date Time