from ch17.services import calculator as cal
# ch17.services 패키지로부터 calculator를 cal이라는 이름으로 임포트

def main():
    print('add(10,2) -> ', cal.add(10, 2))
    print('sub(10,2) -> ', cal.substruct(10, 2))
    print('mul(10,2) -> ', cal.multiply(10, 2))

main()