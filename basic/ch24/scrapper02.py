import requests

from bs4 import BeautifulSoup

res = requests.get("http://book.naver.com")

# html.parser(기본)보다 더 강력한 lxml 많이 사용함
soup = BeautifulSoup(res.text, 'lxml')

a_tag = soup.a
div_tag = soup.div

print("type(div_tag)->", type(div_tag))
print("div_tag->", div_tag)

