import os

print("os.getcwd()->", os.getcwd()) # 현재 폴더 C:\PycharmProject\Sources\basic\ch23 를 출력
filename = "t.txt"


try:
    f = open(filename, 'r') # r(read)로 읽어오려고 하는데 파일이 없으면 IOError 발생
except IOError:
    msg = "IOError"
    print(msg)
else:
    a = float(f.readline())
    print("a=>", a)
    try:
        answer = 1.0 / a
    except ZeroDivisionError as e:
        print("Zero division error occurred")
        print("msg -> ", str(e))
    else:
        print("answer -> ", answer)
    finally:
        print("finally")
        f.close()
    