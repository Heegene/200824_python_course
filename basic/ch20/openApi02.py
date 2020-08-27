import requests

headers = {
    'X-Naver-Client-Id' : 'RkLQo7eDF4QVrC93IQzp',
    'X-Naver-Client-Secret' : 'KDvxQ1hq0N'
}

payLoad = {
    'query' : '파이썬',
    'display' : 5, # 보여줄 결과 수
}

url = 'https://openapi.naver.com/v1/search/blog' # json 결과

res = requests.get(url, headers=headers, params=payLoad)

print('request sended')

# 응답이 json 형태로 옴
print(res.json())

result = res.json()['items'][2]['title']
print('result 번째 title만 가져옴')
print(result)