# Selenium 과 PhantomJS에서 CSS3 Selector 이용하기
# daum News의 header 부분을 crawling
from selenium import webdriver

# 드라이버 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromedriver = 'C:/PyCharmProject/Sources/selenium/chromedriver_win32/chromedriver.exe' # 윈도우
# chromedriver = '/usr/local/Cellar/chromedriver/chromedriver' # 맥
driver = webdriver.Chrome(chromedriver)

driver.get('http://v.media.daum.net/v/20170202180355822')

title_data = driver.find_element_by_css_selector('html head title')
print("html head title-->" , title_data.get_attribute('text'))

# title_data = driver.find_element_by_css_selector('html > title')
# # head 태그 안에 있는 title 정보는 get_attribute('text') 메서드로 추출할 수 있습니다.
# print("html > title-->" ,title_data.get_attribute('text'))

contents = driver.find_element_by_css_selector("div#harmonyContainer")
# body 안에 있는 태그 요소는 .text 로 추출할 수 있습니다. (출력이 잘 안되면, 둘다 써보셔도 좋습니다.)
print("div#harmonyContainer-->" ,contents.text)


# role attribute가 navigation인 div태그
nav = driver.find_element_by_css_selector("div[role='navigation']")
print("div[role='navigation']->", nav.text)

i = 0
for p in contents.find_elements_by_tag_name('p'):
    i +=1
    print (i , p.text)

driver.quit()