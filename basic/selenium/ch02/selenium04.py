# Selenium 과 CSS3 Selector 이용하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# 드라이버2 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromedriver2 = 'C:/PyCharmProject/Sources/selenium/chromedriver_win32/chromedriver.exe' # 윈도우
# chromedriver = '/usr/local/Cellar/chromedriver/chromedriver' # 맥
driver = webdriver.Chrome(chromedriver2)

driver.get('http://v.media.daum.net/v/20170202180355822')

# 클래스가 tit_view인 h3태그
title = driver.find_element_by_css_selector("h3.tit_view")
print (title.text)

driver.quit()