func = [lambda x,y : x+y,
        lambda x,y : x-y,
        lambda x,y : x*y,
        lambda x,y : x/y]

def menu():
    print("0, add")
    print("1, sub")
    print("2. mul")
    print("3. div")
    print("4. quit")
    return input("select menu")

while 1:
    sel = int(menu())
    print("sel->", sel)
    print("len(func)->", len(func))
    if sel < 0 or sel > len(func): # 0보다 작은 값이거나 4보다 큰 경우
        continue
    if sel == len(func):
        break
    x = int(input('First operand: \n'))
    y = int(input('Second operand: \n'))
    print('Result = ', func[sel](x,y))