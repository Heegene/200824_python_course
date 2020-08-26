from idlelib.idle_test.test_format import Editor


class Person:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone
    def __str__(self):
        return '<Person %s %s>' % (self.name, self.phone)


class Employee(Person):
    def __init__(self, name, phone, position, salary):
        Person.__init__(self, name, phone)
        self.position = position
        self.salary = salary

p1 = Person("이콩이", 1498)
print("p1.name -> ", p1.name) # 이콩이 출력

m1 = Employee("김콩이", 5564, "평택강아지", 200)
m2 = Employee("오콩이", 8546, "청주강아지", 300)
print("m1.name, m1.position-> ", m1.name, m1.position) # 김콩이 평택강아지
print("m1->" , m1) # Person 김콩이 5564 (person을 상속받았으므로 person의 str 이 호출됨)
print("m2.name, m2.position-> ", m2.name, m2.position) # 오콩이 청주강아지
print("m2->" , m2) # Person 오콩이 8546

