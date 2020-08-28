# Selenium 과 xpath Selector 이용하기
from selenium import webdriver

# 드라이버 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromedriver = 'C:/PyCharmProject/Sources/selenium/chromedriver_win32/chromedriver.exe' # 윈도우
# chromedriver = '/usr/local/Cellar/chromedriver/chromedriver' # 맥
driver = webdriver.Chrome(chromedriver)
driver.get('http://v.media.daum.net/v/20170922175202762')

title = driver.find_element_by_xpath("//title") # 문서내의 어떤 태그든지 가능

# head 태그 안에 있는 title 정보는 get_attribute('text') 메서드로 추출할 수 있습니다.
print ("find_element_by_xpath  //title-->", title.get_attribute('text'))


driver.get('http://v.media.daum.net/v/20170202185812986')

#soup.find('h3', attrs = {'class' : 'tit_s'})
title_content = driver.find_element_by_xpath("//h3[@class='tit_view']")

# body 안에 있는 태그 요소는 .text 로 추출할 수 있습니다. (출력이 잘 안되면, 둘다 써보셔도 좋습니다.)
print ("find_element_by_xpath  //h3[@class='tit_view'-->", title_content.text)

driver.quit()