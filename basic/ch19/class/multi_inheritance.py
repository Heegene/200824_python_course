class Add:
    def add(self, n1, n2):
        return n1 + n2


class Mul:
    def multi(self, n1, n2):
        return n1 * n2

class Calculator(Add, Mul):
    def sub(self, n1, n2):
        return n1 - n2



cal = Calculator()
print(cal.add(1,2)) # 3 출력
print(cal.multi(3,2)) # 6 출력
print(cal.sub(4,2)) # 2 출력
