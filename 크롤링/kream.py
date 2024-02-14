from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#키보드 입력라던지 어떠한 동작과 관련된 기능을 쓰기위한 패키지
from selenium.webdriver.common.keys import Keys
#클래스, 아이디, css_selector를 이용하고자 할때
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

options = Options()
options.add_argument(f"user-agent={user_agent}")
options.add_experimental_option('detach', True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('excludeSwitches', ['enable-automation'])

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://kream.co.kr/"
search_key_word_count = int(input("검색어 갯수를 입력해주세요: "))
brands = [input("검색을 원하는 브랜드를 입력해주세요 : ") for _ in range(search_key_word_count)]
product = input("원하는 상품 종류를 입력하세요 : ")

count = 0

for count in range(search_key_word_count):
    driver.get(url)
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, ".search_btn_box").click()
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(brands[count])
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
    time.sleep(1)

    for i in range(20) :
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)
        driver.save_screenshot # 스크린샷 찍는 기능 / 경로 + / 파일 이름 및 형색 생성
        driver.save_screenshot("/Users/sampark/Desktop/oz_class_backend/크롤링/kream_img/"+brands[count]+str(i)+".png")

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")


    items = soup.select(".item_inner")

    rank = 1


    for i in items:
        product_name = i.select_one(".translated_name")
        product_price = i.select_one(".amount")
        product_brand = i.select_one(".product_info_brand.brand")
        product_selling = i.select_one(".status_value")
        if product in product_name.text:
            print(f'--{brands[count]} {rank}번--')
            print(f'브랜드 : {product_brand.text}')
            print(f'상품명 : {product_name.text}')
            print(f'가격 : {product_price.text}')
            print(f'{product_selling.text}회')
            print()
            
            rank += 1
    
    count += 1

driver.quit()