try:
    print("1.0 / 1.0" , 1.0 / 1.0)
    number = float("hello")
    print("number -> ", number)
except ZeroDivisionError:
    print("zero division error 발생")
except ValueError as e:
    print("Not a Number " + str(e))

