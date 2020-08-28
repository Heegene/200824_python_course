#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 드라이버 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromedriver = 'C:/PyCharmProject/Sources/selenium/chromedriver_win32/chromedriver.exe' # 윈도우
driver = webdriver.Chrome(chromedriver)

driver.get('https://news.v.daum.net/v/20170202185812986')

# 클래스가 tit_view인 h3태그
title = driver.find_element_by_tag_name('h3')
print (title.text)

# 1.tag name
titles = driver.find_elements_by_tag_name("h3")
for eTitle in titles:
    print("h3->", eTitle.text)  # selenium에는 text로 보여줌


# 2. class name
smallTitle = driver.find_element_by_class_name("gnb_comm")
print("sTitle->",smallTitle.text)  # selenium에는 text로 보여줌

driver.quit()