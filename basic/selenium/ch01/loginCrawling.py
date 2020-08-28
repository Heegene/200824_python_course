#  <<<  한빛미디어 홈페이지(http://www.hanbit.co.kr) 마일리지 크롤링   >>>
#    1.  마일리지를 확인하기 위해 로그인 정보가 필요함
#    2.  세션으로 관리되고 있음을 코드를 통해 확인
#    3.  세션 정보를 획득하고, 이를 사용해서 마일리지 페이지에 접근하여 마일리지 점수 확인
#  http://www.hanbit.co.kr/member/login.html
#  form 태그를 이해할 필요가 있음 (http://pythonscraping.com/pages/files/form.html)
#  form 태그를 통해 ID/PW가 전달되는 것이 일반적이므로 해당 코드 확인 (웹브라우저에서 해당 웹페이지 소스보기로 확인)
# 즉, 버튼을 누르면 login_proc.php 웹페이지에 m_id 값과 m_passwd 값을 넣어 전송해줌
# 마일리지는 http://www.hanbit.co.kr/myhanbit/myhanbit.html 페이지에서 CSS Selector로 확인

import re
import requests
from bs4 import BeautifulSoup
login_url = 'http://www.hanbit.co.kr/member/login_proc.php'

user = ''
password = ''

# requests.session 메서드는 해당 reqeusts를 사용하는 동안 cookie를 header에 유지하도록 하여
# 세션이 필요한 HTTP 요청에 사용됩니다.
session = requests.session()

params = dict()
params['m_id'] = user
params['m_passwd'] = password

# javascrit(jQuery) 코드를 분석해보니, 결국 login_proc.php 를 m_id 와 m_passwd 값과 함께
# POST로 호출하기 때문에 다음과 같이 requests.session.post() 메서드를 활용하였습니다.
# 실제코드: <form name="frm"  id="frm"  action="#" method="post">
res = session.post(login_url, data = params)

# 응답코드가 200 즉, OK가 아닌 경우 에러를 발생시키는 메서드입니다.
res.raise_for_status()

# 'Set-Cookie'로 PHPSESSID 라는 세션 ID 값이 넘어옴을 알 수 있다.
# print(res.headers)

# cookie로 세션을 로그인 상태를 관리하는 상태를 확인해보기 위한 코드입니다.
# print(session.cookies.get_dict())

# 여기서부터는 로그인이 된 세션이 유지됩니다. session 에 header에는 Cookie에 PHPSESSID가 들어갑니다.
mypage_url = 'http://www.hanbit.co.kr/myhanbit/myhanbit.html'
res = session.get(mypage_url)

# 응답코드가 200 즉, OK가 아닌 경우 에러를 발생시키는 메서드입니다.
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

# Chrome 개발자 도구에서 CSS SELECTOR를 통해 간단히 가져온 CSS SELECTOR 표현식을 사용
# he_coin = soup.select_one('#container > div > div.sm_mymileage > dl.mileage_section2 > dd > span')

# a태그이면서 href 속성을 갖는 경우 탐색, 리스트 타입으로 links 변수에 저장됨
html = soup.select('html')
print ('html-->', html)
links = soup.select('a[href]')

# 다음과 같이 class를 .mileage_section2 로 그리고 그 하부 태그중에 span이 있다는 식으로 표현도 가능함
# he_coin = soup.select_one('.mileage_section2 span')

# print ('mileage is', he_coin.get_text())

for link in links:
    # print (link) # <a class="link_services link_services2" href="http://sports.media.daum.net/sports">스포츠</a>
    # print (link['href']) # http://sports.media.daum.net/sports
    if re.search('http://\w+', link['href']):  # http:// 문자열 이후에 숫자 또는 문자[a-zA-Z0-9_]가 한 개 이상 있는 데이터와 매치됨
        print(link['href'])