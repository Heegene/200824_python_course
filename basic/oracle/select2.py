import cx_Oracle

from oracle.insert import cursor

i = 0
with open('C:\PycharmProject\Sources\basic\oracle\emp3.json', 'w', encoding="UTF-8") as make_file:
    text="["
    for empno, ename in cursor:
        if i == 0:
            text1 = "{'empno' : '%s', 'ename' : '%s'}" % (empno, ename)
        else :
            text1 = ", {'empno' : '%s', 'ename' : '%s'}" % (empno, ename)
        text = text + text1
        i = i + 1
