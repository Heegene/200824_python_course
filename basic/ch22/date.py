from datetime import date
from datetime import time

def calc_date(yy, mm, dd):
    # date create
    c_date = date(yy, mm, dd)
    return c_date


def calc_time(hr, mi, sc):
    #time create
    c_time = time(hr, mi, sc)
    return c_time

def main():
    #date
    yy = 2019
    mm = 8
    dd = 20
    hr = 22
    mi = 50
    sc = 59

    rDate = calc_date(yy, mm, dd)
    print('rDate => ', format(rDate))
    print('rDate.month -> ', format(rDate.month))
    print('rDate.day -> ', format(rDate.day))
    print('rDate.year -> ', format(rDate.year))

    #time계산
    rTime = calc_time(hr, mi, sc)
    print('rTime-> {}'.format(rTime))
    print('rTime-> {}'.format(rTime.hour))
    print('rTime-> {}'.format(rTime.minute))
    print('rTime-> {}'.format(rTime.second))

    with open('dateWrite.txt', 'w', encoding="utf-8", newline='') as file:
        strDate = rDate.strftime('%Y/%m/%d')
        file.write(strDate)

if __name__== '__main__':
    main()


