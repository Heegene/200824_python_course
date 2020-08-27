from datetime import date
from datetime import time

def calc_date(yy, mm, dd):
    # date Create
    c_date = date(yy, mm, dd)
    return c_date

def calc_time(hr, mi, sc):
    # time Create
    c_time = time(hr, mi, sc)
    return c_time

def main():
    # date
    yy = 2020
    mm = 8
    dd = 20
    #time
    hr = 22
    mi = 50
    sc = 57
    # Date 계산
    rDate = calc_date(yy, mm, dd)
    print('rDate-> {}'.format(rDate))
    print('rDate.month-> {}'.format(rDate.month))
    print('rDate.day-> {}'.format(rDate.day))
    print('rDate.year-> {}'.format(rDate.year))
    # time  계산
    rTime = calc_time(hr, mi, sc)
    print('rTime-> {}'.format(rTime))
    print('rTime.hour-> {}'.format(rTime.hour))
    print('rTime.minute-> {}'.format(rTime.minute))
    print('rTime.second-> {}'.format(rTime.second))

    with open('dateWrite.txt', 'w', encoding='utf-8', newline='') as file:
        strDate = rDate.strftime('%Y/%m/%d')
        file.write(strDate)


if __name__ == '__main__':
    main()
