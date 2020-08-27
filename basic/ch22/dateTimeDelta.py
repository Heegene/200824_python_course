# datetime에 하루(1day)를 더하고 싶다면 datetime.timedelta를 이용
# 1주	datetime.timedelta(weeks=1)
# 1일	datetime.timedelta(days=1)
# 1시간	datetime.timedelta(hours=1)
# 1분	datetime.timedelta(minutes=1)
# 1초	datetime.timedelta(seconds=1)
# 1밀리초	datetime.timedelta(milliseconds=1)
# 1마이크로초	datetime.timedelta(microseconds=1)
import datetime

now = datetime.datetime.now()
print('now->', now)  # current date

# 그냥 시간을 설정할 때
setDate = datetime.timedelta(hours=5, minutes=30)
print('setDate->', setDate)  # set Date
tomorrow = now + datetime.timedelta(days=1)
print('tomorrow->', tomorrow)  # current date + 1

# 1주 더하기
weekAppend = now + datetime.timedelta(weeks=1)
print('weekAppend->', weekAppend)  # current date + 1 week

# 1주 빼기
weekBefore = now + datetime.timedelta(weeks=-1)
print('weekBefore->', weekBefore)  # current date - 1 week
