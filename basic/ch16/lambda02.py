g = lambda x, y:x + y
print("g(1,2) -> ", g(1,2)) # 3 출력

incr = lambda x, inc = 1: x + inc
print("incr(10)-> ", incr(10)) # 11 출력
print("incr(10, 5)->", incr(10,5)) # 15 출력