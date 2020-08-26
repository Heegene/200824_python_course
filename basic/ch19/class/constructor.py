class Animal:

    var3 = 'var3 안녕하세요'
    def __init__(self):
        self.var1 = 'var1 안녕하세요'
        print("Animal 인스턴스 객체가 생성되었음")


# 권장사항: 클래스를 만든 뒤에는 두 줄을 띄워야 함
cat = Animal() # 인스턴스 객체 생성
print('cat.var1', cat.var1) # var1값 출력
print(type(cat)) # 타입이 main_animal로 나옴
print('Animal().var3 -> ', Animal.var3)


