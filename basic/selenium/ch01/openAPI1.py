# 파이썬 표준 urllib2 모듈은 필요한 HTTP 기능을 거의 제공하지만, 이제 너무 뒤떨어져 있음
# 이 API는 과거에, 과거의 웹을 위해 만들어졌습니다. urllib2를 사용하려면 정말 단순한 일
#  하나만 하려 해도 할 일이 너무 많음
# 이제 requests 라이브러리를 활용한 크롤링 코드 권장(간결함)

import requests

client_key = 'CsODwdUTyG9vOI1uIeIf'
client_secret = 'YmIx0GW8JG'
# 별도 quote_plus() 메서드등 처리할 필요 없음. requests 객체가 알아서 해줌
naver_url = 'https://openapi.naver.com/v1/search/news.json?query=스마트폰'

header_params = {"X-Naver-Client-Id": 'j513HictYVPoWEl27Yor',
                 "X-Naver-Client-Secret":'I0m7fwb6Cn', }
# headers= header_params 는 header 변경시에만 필요하고, 그렇지 않으면, requests.get(원하는 URL) 만 해도 됨
response = requests.get(naver_url, headers = header_params)
# 별도 json.loads() 라이브러리 메서드 사용하지 않아도, reqeusts 라이브러리에 있는 json() 메서드로 간단히 처리 가능함
# print(response.json())
# print(response.text)

# HTTP 응답 코드는 status_code 에 저장됨
if(response.status_code == 200):
    data = response.json()
    print(data['items'][0]['title'])
    print(data['items'][0]['description'])
else:
    print("Error Code:" + response.status_code)