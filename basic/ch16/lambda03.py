print("---------------------------")
vargs = lambda x, *args: args+args # *args 는 가변 함수. x는 1이 되고 2,3,4,5는 *args 로 받아짐
# 그래서 2,3,4,5가 한번 더 반복되는것
# tuple 이므로 tuple 의 더하기 연산은 한번 더 반복됨
print("vargs(1,2,3,4,5) ->", vargs(1,2,3,4,5) ) # 2,3,4,5,2,3,4,5 출력