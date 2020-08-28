from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# 드라이버 생성 방법1 (selenium)
chromedriver = 'C:/PyCharmProject/Sources/selenium/chromedriver_win32/chromedriver.exe' # 윈도우
driver = webdriver.Chrome(chromedriver)

# 드라이버 생성 방법2 (phantomJS)
# driver = webdriver.PhantomJS('C:/PyCharmProject/phantomjs-2.1.1-windows/bin/phantomjs.exe') # 윈도우
driver.get('http://v.media.daum.net/v/20170202180355822')
try:
    # id가 cMain인 tag를 10초 내에 검색, 그렇지 않으면 timeoutexception 발생
    element = WebDriverWait(driver, 10).until(
        # By.ID 는 ID로 검색, By.CSS_SELECTOR 는 CSS Selector 로 검색
        EC.presence_of_element_located((By.ID, "cMain"))
    )
    print("element.text->" , element.text)
    #print("id가 cMain인 tag element->", element.text)

except TimeoutException:
    print("해당 페이지에 cMain 을 ID 로 가진 태그가 존재하지 않거나, 해당 페이지가 10초 안에 열리지 않았습니다.")

finally:
    driver.quit()