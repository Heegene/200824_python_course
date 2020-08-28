#  selenium --> PhantomJS사용 Conversion
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 드라이버 생성 방법1 (selenium)
# chromedriver = 'C:/PyCharmProject/Sources/selenium/chromedriver_win32/chromedriver.exe' # 윈도우
# driver = webdriver.Chrome(chromedriver)


# 드라이버 생성 방법2 (phantomJS)
#driver = webdriver.PhantomJS('C:/PyCharmProject/phantomjs-2.1.1-windows/bin/phantomjs.exe') # 윈도우


# 드라이버 생성 방법3 (Headless Chrome )
# 설치는 따로 필요없음 , 아래 3줄 선언
chromedriver = 'C:/PyCharmProject/Sources/selenium/chromedriver_win32/chromedriver.exe' # 윈도우
headlessOptions = webdriver.ChromeOptions()
headlessOptions.add_argument('headless')
# option 추가
headlessOptions.add_argument('disable-gpu')             # gpu 사용 안함
#headlessOptions.add_argument('window-size=1920*1080')  # window Size 설정
driver = webdriver.Chrome(chromedriver , options=headlessOptions)

driver.get("http://www.python.org")

print ("driver.current_url-->", driver.current_url)
print ("driver.title-->", driver.title)

elem = driver.find_element_by_name("q")

# input 텍스트 초기화
elem.clear()

# 키 이벤트 전송
elem.send_keys("python")

# 엔터 입력
elem.send_keys(Keys.RETURN)
# dir(keys)로 Key종류 확인가능
print("dir(Keys)-->", dir(Keys))

# 스크린샷도 찍을 수 있습니다.
# driver.set_window_size(1400, 1000)
# elem.screenshot("pycon_event.png")
# assert "No results found." not in driver.page_source

driver.quit()