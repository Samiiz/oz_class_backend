from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pymysql






# connection = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='samiiz',
#     db='kream',
#     charset='utf8mb4',
#     cursorclass=pymysql.cursors.DictCursor
# )


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

options = Options()
options.add_argument(f"user-agent={user_agent}")
options.add_experimental_option('detach', True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('excludeSwitches', ['enable-automation'])

service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=service, options=options)

base_url = "https://kream.co.kr"

남성 = {
    "의류" : "2489",
    "신발" : "2487", 
    "자켓" : "2573"
}
여성 = {
    "신발" : "2488",
    "의류" : "2490",
    "자켓" : "2571"
}
이외 = {
    "지갑" : "2570",
    "백팩" : "3326"
}

CateList = [남성, 여성, 이외]
fullList = ["남성", "여성", "이외"]

Cn = 0
num = 1
for one in CateList:
    for cate, urlNum in one.items():
        url = "https://kream.co.kr/exhibitions/"
        url += urlNum
        categiory = cate
        browser.get(url)
        print(f'{num} --- {categiory}')

        print("-------------------")
        print("스크롤 중..")

        for i in range(15) :
                browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
                time.sleep(0.3)
        
        print("스크롤 종료.")
        print("-------------------")

        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")


        items = soup.select(".item_inner")

        n = 1
        for SomeProduct in items:
            page = SomeProduct["href"]
            print(f'{n}번째 {fullList[Cn]}{cate}입니다.')
            try:
                browser.get(base_url + page)

                time.sleep(1)

            except:
                 print(f'{n}번째 {fullList[Cn]}{cate}가져오기 실패. 다음상품으로 넘어갑니다.')
                 pass
            

            n += 1





        num += 1
    Cn +=1

browser.quit()