# 1. yesterday.txt 파일을 읽고
# 한 라인씩 읽어서 원문 한라인, 해석된 라인 한라인 씩 해석

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

# encText = urllib.parse.quote("번역할 문장을 입력하세요")
# data = "source=ko&target=en&text=" + encText

# 문장번역 URL 지정
# url = "https://openapi.naver.com/v1/language/translate"
# 위의 url은 구 주소로, api가 동작하지 않으면 api 주소가 그대로인지 확인하기
url = "https://openapi.naver.com/v1/papago/n2mt"

f = open('C:\\PycharmProject\\Sources\\basic\\ch20\\Yesterday.txt', 'r')
w = open('C:\\PycharmProject\\Sources\\basic\\ch20\\Yesterday3.txt', 'w')

while True:
    line = f.readline()
    payLoad = {
        'source': 'en',
        'target': 'ko',
        'text': line,
    }
    if not line: break
    print(line)
    req = Request('Post', url, data=payLoad, headers=headers)
    prepared = req.prepare()
    res = s.send(prepared)
    result = (res.json()['message']['result']['translatedText'])+'\n'
    print(result)
    w.write(line)
    w.write(result)

f.close()
w.close()
