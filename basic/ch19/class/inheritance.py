# 클래스의 상속
class Add:
    def add(self, n1, n2):
        return n1 + n2


class Calculator(Add): # Add 클래스 상속
    def sub(self, n1, n2):
        return n1 - n2


cal = Calculator()

print(cal.add(1,2)) # 3 출력
print(cal.sub(1,2))

obj2 = Add()
print(obj2.sub(1,2))

