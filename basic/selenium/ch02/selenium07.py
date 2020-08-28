# xpath
from selenium import webdriver

# 드라이버 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromedriver = 'C:/PyCharmProject/Sources/selenium/chromedriver_win32/chromedriver.exe' # 윈도우
# chromedriver = '/usr/local/Cellar/chromedriver/chromedriver' # 맥
driver = webdriver.Chrome(chromedriver)
driver.get('https://news.v.daum.net/v/20170202180355822')
# div 해당 tag의 속성 role값이 navigation 인것
head_title = driver.find_element_by_css_selector("div[role='navigation']")
print ("head_title.text-->",  head_title.text)


driver.quit()