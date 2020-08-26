# 멤버변수

class MyClass:
    var = '왈왈'
    def __init__(self):
        pass


    def sayHello(self):
        param1 = "안녕" # 인스턴스 멤버변수
        print("sayHello param1", param1)
        print("sayHello self.var", self.var)



love = MyClass()
print(love.var) # 왈왈 출력
#print(love.param1)
love.sayHello() # 안녕 출력

love3 = MyClass()
love.var = '어떻게 사랑이 변하니'

print('love.var->', love.var) # 어떻게 사랑이 변하니 출력
print('love3.var -> ', love3.var) # 클래스 멤버변수라 할지라도 해당 인스턴스에만 영향미치고
# love3은 그대로 값을 가지고 있어서 왈왈 출력
print("MyClass().var", MyClass().var) # 왈왈 출력
