import re

# 정규식에 search 사용 -> 매칭되는 첫 번째 패턴 반환
# 전화번호 패턴

phonenum_regex = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
mo = phonenum_regex.search("My contact number is 010-1122-3344")
print("mo.group() -> " , mo.group())
print("---2. 괄호를 사용, 정규식에 group 생성, (\d\d\d) -> Group 함수 사용 --")

# 2. 괄호를 사용, 정규식에 group 생성, (\d\d\d) -> Group 함수 사용

phonenum_regex = re.compile(r'(\d\d\d)-(\d\d\d\d)-(\d\d\d\d)')
mo=phonenum_regex.search("My contact number is 010-1234-4567")
print("mo_group(1) -> ", mo.group(1))
print("mo_group(2) -> ", mo.group(2))
print("mo_group(3) -> ", mo.group(3))

# 튜플로 전달
print("mo.groups() -> ", mo.groups())

# 3. findall -> 매칭되는 모든 패턴 list 변환
phonenum_regex = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
mo = phonenum_regex.findall("cell: 010-1234-4567 work: 010-4432-2345")
print("3. mo-> " , mo)
