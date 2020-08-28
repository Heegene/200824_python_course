# Selenium: 웹을 테스트하기 위한 프레임워크
# 공식 홈페이지(http://www.seleniumhq.org/)
# Selenium with Python : http://selenium-python.readthedocs.io/index.html
# 사전준비 (Selenium 설치)
# 1. Selenium 인스톨: pip install selenium
# 2. 웹드라이버 인스톨: 웹 테스트 자동화를 위해 제공되는 툴(각 browser및 os 별로 존재)
# - selenium - 테스트 코드를 사용하여 브라우져에서의 액션을 테스트할 수 있게 해주는 툴
# - Firefox, chromedriver 등 각 브라우져마다 웹드라이버 다운로드 가능
# + https://sites.google.com/a/chromium.org/chromedriver/ (Chrome 브라우저용)
# + https://github.com/mozilla/geckodriver/releases (Firefox 브라우저용)
# 확인: 설치 디렉토리를 알아두어야 함

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 드라이버 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromedriver = 'C:/PyCharmProject/Sources/selenium/chromedriver_win32/chromedriver.exe' # 윈도우
# chromedriver = '/usr/local/Cellar/chromedriver/chromedriver' # 맥
driver = webdriver.Chrome(chromedriver)

# 크롤링할 사이트 호출
driver.get("http://www.python.org")

print("driver.title->" , driver.title)
# Selenium은 웹테스트를 위한 프레임워크로 다음과 같은 방식으로 웹테스트를 자동으로 진행함 (참고)
# 만약 driver.title 안에  "Python"  String가 없으면 자동 종료
assert "Python" in driver.title

# <input id="id-search-field" name="q" 검색창 name으로 검색하기
# 태그 name으로 특정한 태그를 찾을 수 있음 -> 최초
elem = driver.find_element_by_name("q")

# input 텍스트 초기화
# elem.clear()

# 키 이벤트 전송가능함
# 태그가 input 태그이므로 입력창에 키이벤트가 전달되면, 입력값이 자동으로 작성됨
elem.send_keys("python")

# 태그가 input 태그이므로 엔터 입력시 form action이 진행됨
elem.send_keys(Keys.RETURN)

# Selenium은 웹테스트를 위한 프레임워크로 다음과 같은 방식으로 웹테스트를 자동으로 진행함 (참고)
# 만약 driver.page_source 안에  "No results found"  String가 있으면 자동 종료(Error 발생)
assert "No results found." not in driver.page_source

# 다음코드로 넘어가지 않고 명시적으로 일정시간을 기다릴 수 있음
# 20초 기다림
time.sleep(20)

print ("driver.current_url-->", driver.current_url)
print ("driver.title-->", driver.title)

# 크롬 브라우저 닫기 가능함
driver.quit()