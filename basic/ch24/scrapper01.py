import requests

res = requests.get("http://book.naver.com")

# request해서 response 내의 모든 태그 가져옴
print("res.header->", res.headers)
# dict type
print("res.text-> ", res.text)


