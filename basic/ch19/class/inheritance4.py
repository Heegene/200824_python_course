class Animal:
    def cry(self):
        print("ㅠㅠ")


class Dog(Animal):
    def cry(self):
        print("왈왈")


class Duck(Animal):
    def cry(self):
        print("꽉꾸악")


class Fish(Animal):
    pass
# Fish는 cry 없으므로 Animal 내용 그대로 상속


# in 뒤에는 튜플 안에 객체 3개 존재
# each 의 객체 형 동적으로 결정됨
for each in (Dog(), Duck(), Fish()):
    each.cry() # 왈왈, 꽉꾸악, ㅠㅠ 출력 


