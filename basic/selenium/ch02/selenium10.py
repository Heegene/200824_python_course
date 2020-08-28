# https://twitter.com에 선 가입
# https://twitter.com/ 에 자동 로그인하고 그 내용을 가져오기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 드라이버 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromedriver = 'C:/PyCharmProject/Sources/selenium/chromedriver_win32/chromedriver.exe' # 윈도우
# chromedriver = '/usr/local/Cellar/chromedriver/chromedriver' # 맥
driver = webdriver.Chrome(chromedriver)

driver.get('http://www.twitter.com')

id =  driver.find_element_by_name("session[username_or_email]")
id.clear()
id.send_keys("@apple577049051")
pw =  driver.find_element_by_name("session[password]")
pw.clear()
pw.send_keys("apple7645")
# 태그가 input 태그이므로 엔터 입력시 form action이 진행됨
pw.send_keys(Keys.RETURN)

# 일정시간
time.sleep(10)

i = 0
# 1. div안의 id="harmonyContainer" 해당 속성 가져옴
# 2. class name
data = driver.find_elements_by_class_name("css-901oao")
# 1. div안의 id="harmonyContainer" 해당 속성 가져옴
# data = driver.find_element_by_xpath("//span[@class='css-901oao']")
# print ( ". data->", data.text)
# 1안의 tag_name이 p인것을 순환하며 가져옴
for p in data:
    i +=1
    print (i , " : ", p.text)



driver.quit()