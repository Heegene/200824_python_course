# Web Page Get
import requests
# Web Page 분석 Lib
from bs4 import BeautifulSoup
import re

# 1) reqeusts 라이브러리를 활용한 HTML 페이지 요청
# 1-1) res 객체에 HTML 데이터가 저장되고, res.content로 데이터를 추출할 수 있음
res1 = requests.get('http://v.media.daum.net/v/20170615203441266')

# print(res.content)
# 2) HTML 페이지 파싱 BeautifulSoup(HTML데이터, 파싱방법)
# 2-1) BeautifulSoup 파싱방법
soup = BeautifulSoup(res1.content, 'html.parser')

# 3) 필요한 데이터 검색
title = soup.find('title')

# 4) 필요한 데이터 추출
print("title->", title.get_text())

# 태그가 아닌 문자열 자체로 검색
# 문자열, 정규표현식 등등으로 검색 가능
# 문자열 검색의 경우 한 태그내의 문자열과 exact matching인 것만 추출
# 이것이 의도한 경우가 아니라면 정규표현식 사용
# HTML DOM 트리 구성하기 (html5lib)
#  html이라는 변수에 담긴 문자열을 분석하여 트리 구조로 만들면 원하는 내용을 쉽게 추출
#  html5lib는 HTML 문서를 트리구조로 분석해주는 라이브러리
res2 = requests.get('http://v.media.daum.net/v/20170518153405933')
soup = BeautifulSoup(res2.content, 'html5lib')

print ("string='오대석'-->", soup.find_all(string='오대석'))
print ("string=이주의해시태그-#네이버-클로바]쑥쑥 크는 네이버 AI', '오대석'-->", soup.find_all(string=['[이주의해시태그-#네이버-클로바]쑥쑥 크는 네이버 AI', '오대석']))
print ("string='AI'-->", soup.find_all(string='AI'))
print ("string=re.compile('AI')-->", soup.find_all(string=re.compile('AI'))[0])
# print (soup.find_all(string=re.compile('AI')))