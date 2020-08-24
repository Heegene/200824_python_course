#string1.py

pin = '881120-1068234'
# 없으면 처음부터 : 6 -> 미만의 문자열
yymmdd = pin[:6]
num = pin[7:] # 7 포함 끝까지
print(yymmdd) # 881120
print(num) #1068234