class HousePark:
    lastname = "Park "
    def __init__(self, name):
        self.fullname=self.lastname+name
    def travel(self, where):
        print("%s %s 로 여행을 갑니다." % (self.fullname, where))

    def walk(self, other):
        print("%s, %s 와 함께 산책합니다." % (self.fullname, other.fullname))

    def feed(self, other):
        print("%s, %s 밥을 줍니다." % (self.fullname, other.fullname))

    def __add__ (self, other):
        print("%s, %s 입양했습니다." % (self.fullname, other.fullname))

    def add3(self, a, b):
        k = a + b
        print("2덧셈 %d + %d = %d 입니다." % (a, b, k))
    def __sub__(self, other):
        print("%s, %s 밤에는 켄넬에 들어갑니다." % (self.fullname, other.fullname))

class HouseKim(HousePark):
    lastname = "Kim"
    def travel(self, where, day):
        print("%s %s 으로 여행 %d 일 가네" % (self.fullname, where, day))
    ...
    def add3(self, a, b, c, d):
        k = a+b+c+d
        print("4덧셈 %d + %d + %d + %d = %d 입니다." % (a,b,c,d,k))

pey = HousePark("콩이")
julet = HouseKim("KongE")
pey.travel("애견카페")
julet.travel("애견펜션", 3)
pey.walk(julet)
pey + julet
#pey.add(julet)
pey.__add__(julet)
pey.add3(3,5)
#julet.add3(3,5,7)
julet.add3(3,5,7,9)
pey.feed(julet)
pey-julet
