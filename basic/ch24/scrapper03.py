import requests
import lxml


from bs4 import BeautifulSoup

import csv

BASE_URL = 'http://pythonscraping.com'


def create_list_from_table(table_tag):
    # csv 파일 생성을 위해 2중 리스트 생성
    gifts = []

    # header 에 해당하는 첫 번째 rosw 생성
    headers = []
    header_tag = table_tag.find('tr')
    for th_tag in header_tag.find_all('th'): # th에 해당하는 태그를 모두 가져옴
        # space 등 제거
        headers.append(th_tag.text.strip())

    gifts.append(headers)

    print("2.gifts-> %s" % gifts)

    # 본문: 선물 record 작성
    for tr_tag in table_tag.find_all('tr'):
        gift = []
        for td_tag in tr_tag.find_all('td'):
            if td_tag.text.strip() != '':
                # 좌우 공백제거, 개행문자를 공백 변경
                gift.append(td_tag.text.strip().replace('\n', ' '))
            else:
                # text 문자가 없다면 img라 가정하고 img 태그를 가져오기 위한 처리
                gift.append(BASE_URL + td_tag.find('img').get('src')[2:])  # src 속성 내의 값을 가져옴 ../ <- 이후부터

        if not gift:
            continue
        gifts.append(gift)
    print("2.gifts->%s" % gifts)

    return gifts


def create_csv_file(gifts, filename):
    with open(filename, 'w', encoding="UTF-8", newline='') as file:
        writer = csv.writer(file)
        # gifts를 라인단위로 작성
        for line in gifts:
            writer.writerow(line)


def main():
    res = requests.get(BASE_URL+"/pages/page3.html")

    soup = BeautifulSoup(res.text, 'lxml')
    table_tag = soup.find(id='giftList')

    print("table_tag->%s" % table_tag)

    # list 형태로 가져옴
    gifts = create_list_from_table(table_tag)
    # 테이블의 제목부분(아이템, 내용, 가격, 이미지) 가져옴
    # csv 형태의 파일로 작성

    create_csv_file(gifts, 'gifts.csv')
    print("csv compiled")


main()






