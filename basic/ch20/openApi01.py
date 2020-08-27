import requests


# urllib가 core에 있지만 requests 가 있어서 그걸로 많이들 사용함

res = requests.get("https://developers.naver.com/main/")

#json res = res.json()
print("type(res)->", type(res))
print("print res.text->", res.text)

# res를 json 형태를 가진 파이썬의 json 형태로 전환
