# Selenium 과 PhantomJS 활용 다음 뉴스 댓글 가져오기
# 동적 Web Page Loading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# 드라이버 생성 방법1 (selenium)
chromedriver = 'C:/PyCharmProject/Sources/selenium/chromedriver_win32/chromedriver.exe' # 윈도우
driver = webdriver.Chrome(chromedriver)

driver.get('http://v.media.daum.net/v/20170202180355822')

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "alex-area"))
    )
    print(element.text)
except TimeoutException:
    print('''해당 페이지에 alex-area 을 ID 로 가진 태그가 존재하지 않거나, 
            해당 페이지가 10초 안에 열리지 않았습니다 ''')
finally:
    driver.quit()