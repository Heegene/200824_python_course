# Selenium 활용 다음 뉴스 댓글 가져오기2
# 동적 Web Page Loading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
# 드라이버 생성 방법1 (selenium)
chromedriver = 'C:/PyCharmProject/Sources/selenium/chromedriver_win32/chromedriver.exe' # 윈도우
driver = webdriver.Chrome(chromedriver)

driver.get("https://news.v.daum.net/v/20191124103713938?d=y")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "alex-area"))
    )
except:
    print('''댓글관련 Tag가 없습니다 ''')

else:
    loop, count = True, 0
    while loop and count < 10:
        try:
            # 3초안에 더 보기 버튼이 없을수도 있기 때문에 기다림
            element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#alex-area > div > div > div > div.cmt_box > div.alex_more > a > span:nth-child(1)")))
            # 해당 Tag가 있다면 가져옴
            more_button = driver.find_element_by_css_selector("#alex-area > div > div > div > div.cmt_box > div.alex_more > a > span:nth-child(1)")
            webdriver.ActionChains(driver).click(more_button).perform()
            count += 1
            time.sleep(5)
        # 10번 까지 진행
        except TimeoutException:
            loop = False

    comment_box = driver.find_element_by_css_selector("#alex-area > div > div > div > div.cmt_box > ul.list_comment ")
    comment_list = comment_box.find_elements_by_tag_name("li")
    for num, comment_item in enumerate(comment_list):
        print(num, comment_item.find_element_by_css_selector("div p").text)
        # if num < 10:
        #     print(num , comment_item.find_element_by_css_selector("div p").text)
        # else:
        #     break

driver.quit()