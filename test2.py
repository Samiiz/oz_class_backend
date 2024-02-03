from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pymysql






connection = pymysql.connect(
    host='localhost',
    user='root',
    password='samiiz',
    db='kream',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


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
    "신발" : "2487",
    "의류" : "2489",
    "자켓" : "2573"
}
여성 = {
    "신발" : "2488",
    "의류" : "2490",
    "자켓" : "2571"
}
기타 = {
    "지갑" : "2570",
    "백팩" : "3326",
    "신규" : "2082"
}

CateList = [남성, 여성, 기타]
fullList = ["남성", "여성", "기타"]

Cn = 0
num = 1
an = 1
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

        time.sleep(2)

        items = soup.select(".item_inner")

        time.sleep(1)

        n = 1
        for SomeProduct in items:

            category_parents = fullList[Cn]
            category_child = cate
            product_name = SomeProduct.select_one(".translated_name").text
            product_brand = SomeProduct.select_one(".product_info_brand.brand").text.strip()
            product_price = SomeProduct.select_one(".amount").text.strip().replace(",","").replace("원","")

            try:
                if "-" in product_price:
                    product_price = 0
                else :
                    product_price = int(product_price)
            except:
                print(f"{an}가격 오류확인 필요")
                pass

            try:
                if SomeProduct.select_one(".status_value") :
                    product_selling = SomeProduct.select_one(".status_value").text.strip().split()[1].replace(",", "").replace(".", "").replace("만", "000")
                    product_selling = int(product_selling)
                else :
                    product_selling = 0
            except:
                print(f"{an}거래량 오류확인 필요")
                pass

            print(f'{n}번째 {fullList[Cn]}{cate} 데이터 입력중...')
            with connection.cursor() as cursor:

                try:
                    sql = ("""
                        INSERT INTO products (category_parents, category_child, product_name, brand, price, selling)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """)
                    cursor.execute(sql, (category_parents, category_child, product_name, product_brand, product_price, product_selling))
                    connection.commit()

                except:
                    print(f'{n}번째 {fullList[Cn]}{cate} 데이터 입력 오류(총 데이터중 {an}번째)')
                    pass
            time.sleep(0.5)
            n += 1
            an += 1

        num += 1
    Cn +=1

cursor.close()
browser.quit()

# Parent_Category = for문에 따라서 male, female, kidz
# Child_Category = for문에 따라서 아우터 ~ 가구 리빙
# product_name = i.select_one(".translated_name")
# product_price = i.select_one(".amount")
# product_brand = i.select_one(".product_info_brand.brand")
# product_selling = i.select_one(".status_value")
# 북마크 수
# 이미지 .image.full_width