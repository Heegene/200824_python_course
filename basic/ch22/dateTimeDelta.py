import datetime
now = datetime.datetime.now()
print('now -> ', now)

# 시간 설정할때
setDate = datetime.timedelta(hours=5, minutes=30)
print('setDate ->', setDate)

tomorrow = now + datetime.timedelta(days=1)
print('tomorrow -> ', tomorrow)

# 1주 더하기
weekAppend = now + datetime.timedelta(weeks=1)
print('weekAppend ->', weekAppend)

# 1주 빼기
weekBefore = now + datetime.timedelta(weeks=-1)
print("weekBefore->", weekBefore)

