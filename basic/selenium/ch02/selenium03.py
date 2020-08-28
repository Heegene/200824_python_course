# Selenium 과 find_element_by_id 이용하기
# Selenium 과 CSS3 Selector 이용하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 드라이버1 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromedriver = 'C:/PyCharmProject/Sources/selenium/chromedriver_win32/chromedriver.exe' # 윈도우
driver = webdriver.Chrome(chromedriver)
# 크롤링할 사이트 호출
driver.get("http://www.python.org")

# id가 id-search-field 찾기
search = driver.find_element_by_id("id-search-field")
search.clear()
search.send_keys("python")
# 태그가 input 태그이므로 엔터 입력시 form action이 진행됨
search.send_keys(Keys.RETURN)

time.sleep(10)
# Selenium은 웹테스트를 위한 프레임워크로 다음과 같은 방식으로 웹테스트를 자동으로 진행함 (참고)
# 만약 driver.page_source 안에  "No results found"  String가 있으면 자동 종료
assert "No results found." not in driver.page_source

# pycon 검색결과를 보고 싶음 (css_selector 이용)
data = driver.find_elements_by_css_selector("#content > div > section > form > ul > li > h3 > a")
for item in data:
    print(item.text)  # selenium에는 text로 보여줌

driver.quit()