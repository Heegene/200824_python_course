#   <<<    연습문제   >>>
#  다음 사이트에서 링크가 되어 있는 모든 제목을 가져와서 출력합니다.
#  http://media.daum.net/digital/
import requests
from bs4 import BeautifulSoup

res = requests.get('http://media.daum.net/digital/')
soup = BeautifulSoup(res.content, 'html.parser')

# find_all() 메서드를 사용해서 태그와 클래스이름으로 링크가 걸려있는 기사 타이틀을 가져오기
# find_all() 관련된 모든 데이터를 리스트 형태로 추출하는 함수
#link_title = soup.find_all('.link_txt #article_main')
link_title = soup.findAll('a', attrs={'class': 'link_txt'})
for num in range(len(link_title)):
    print(link_title[num].get_text().strip())