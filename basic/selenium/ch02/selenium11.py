# http://pythonscraping.com/pages/files/form.html에 접속
# First name , lastname을 넣고 자동 submit 버튼을 누름
# submit한 Page이동  body내용을 가져옴
# 과제 전달 1
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# 드라이버 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromedriver = 'C:/PyCharmProject/Sources/selenium/chromedriver_win32/chromedriver.exe' # 윈도우
# chromedriver = '/usr/local/Cellar/chromedriver/chromedriver' # 맥
driver = webdriver.Chrome(chromedriver)
driver.get("http://pythonscraping.com/pages/files/form.html")

firstnameField = driver.find_element_by_name("firstname")
lastnameField = driver.find_element_by_name("lastname")
submitButton = driver.find_element_by_id("submit")

firstnameField.send_keys("Gil-Dong")
lastnameField.send_keys("Hong")
submitButton.click()

print(driver.find_element_by_tag_name("body").text)

driver.close()