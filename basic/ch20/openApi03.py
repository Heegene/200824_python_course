#papago  번역
from requests import Request
from requests import Session

s = Session()

# id, 비밀번호

headers = {
    'X-Naver-Client-Id' : 'RkLQo7eDF4QVrC93IQzp',
    'X-Naver-Client-Secret' : 'KDvxQ1hq0N'
}

text = "Yesterday all my troubles seemed so far away"

# dict type

payLoad = {
    'source' : 'en',
    'target' : 'ko',
    'text' : text,
}

# encText = urllib.parse.quote("번역할 문장을 입력하세요")
# data = "source=ko&target=en&text=" + encText

# 문장번역 URL 지정
# url = "https://openapi.naver.com/v1/language/translate"
# 위의 url은 구 주소로, api가 동작하지 않으면 api 주소가 그대로인지 확인하기
url = "https://openapi.naver.com/v1/papago/n2mt"

req = Request('POST', url, data=payLoad, headers=headers)
# 미리 내부적으로 compile
prepared = req.prepare()
# session 객체를 통해 전송
res = s.send(prepared)

print("res.json() -> " , res.json())
print("text -> ", res.json()['message']['result']['translatedText']) # 번역텍스트만 출력됨
