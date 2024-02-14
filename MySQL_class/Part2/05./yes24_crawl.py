from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pymysql
import re
from datetime import datetime

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='samiiz',
    db='yes24',
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

# 1페이지의 링크 데이터 전부 수집하기
    ## 한개의 베스트셀러 링크 수집
# a = browser.find_element(By.CLASS_NAME, 'gd_name').get_attribute('href')
# print(a)

link_list = []
for pageNum in range(1,4):
    print("*"*10, f"현재 {pageNum}페이지 수집 중 입니다.", "*"*10)
    url = f"https://www.yes24.com/Product/Category/BestSeller?CategoryNumber=00{pageNum}&sumgb=06"

    browser.get(url)

    datas = browser.find_elements(By.CLASS_NAME, 'gd_name')

    page_list = [att_href.get_attribute('href') for att_href in datas]
    link_list.extend(page_list)

    time.sleep(0.5)

# 데이터 베이스 연동 후 -> 수집한 데이터를 DB에 저장
contents = 1

with connection.cursor() as cursor:

    for link in link_list:

        browser.get(link)

        title = browser.find_element(By.CLASS_NAME, 'gd_name').text
        # print(f'\n제목 : {title}')

        author = browser.find_element(By.CLASS_NAME, 'gd_auth').text
        # print(f'저자 : {author}')

        publisher = browser.find_element(By.CLASS_NAME, 'gd_pub').text
        # print(f'출판사 : {publisher}')

        publishing = browser.find_element(By.CLASS_NAME, 'gd_date').text

        match = re.search(r'(\d+)년 (\d+)월 (\d+)일', publishing)

        if match:
            year, month, day = match.groups()
            data_obj = datetime(int(year), int(month),int(day))
            publishing = data_obj.strftime('%Y-%m-%d')
        else:
            publishing = '0000-00-00'

        # print(f'출판일 : {publishing}')

        rating = browser.find_element(By.CLASS_NAME, 'yes_b').text
        # print(f'평점 : {rating}점')

        try:
            review = browser.find_element(By.CLASS_NAME, 'txC_blue').text
            if review.isdigit():
                review = int(review.replace(',', ''))
            else:
                review = 0
        except:
            print(f'{contents}번째 책의 "review"의 내용을 재확인 하세요.')
        # print(f'리뷰 : {review}개')

        sales = browser.find_element(By.CLASS_NAME, 'gd_sellNum').text.split(' ')[2]
        sales = int(sales.replace(',', ''))
        # print(f'판매지수 : {sales}권')

        price = browser.find_element(By.CLASS_NAME, 'nor_price').text
        price = int(price.replace(',', '').replace('원', ''))
        # print(f'판매가 : {price}')

        rankings = browser.find_element(By.CLASS_NAME, 'gd_best').text
        parts = rankings.split(' | ')

        if len(parts) == 1:
            ranking = 0
            ranking_weeks = 0
        else:
            try:
                ranking_part = parts[0]
                ranking = int(" ".join(filter(str.isdigit, ranking_part)))

            except:
                ranking = 0

            try:
                ranking_weeks_part = parts[1]
                ranking_weeks = int(" ".join(filter(str.isdigit, ranking_weeks_part.split()[-1])))

            except:
                ranking_weeks = 0

        # if ' | ' in rankings:
        #     ranking = rankings.split(' | ')[0].split(' ')[-1]
        #     ranking_weeks_text = rankings.split(' | ')[1].split(' ')[1:]
        #     ranking_weeks = " ".join(word.upper() for word in ranking_weeks_text)
        #     print(ranking)
        #     print(ranking_weeks)

        # elif rankings:
        #     ranking = rankings.split(' | ')[0].split(' ')[-1]
        #     ranking_weeks = 0
        #     print(ranking)
        #     print(ranking_weeks)

        # else:
        #     ranking = 0
        #     ranking_weeks = 0
        #     print(ranking)
        #     print(ranking_weeks)

        contents += 1

        sql = ("""
            INSERT INTO Books (`title`, `author`, `publisher`, `publishing`, `rating`, `review`, `sales`, `price`, `ranking`, `ranking_weeks`)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """)

        cursor.execute(sql, (title, author, publisher, publishing, rating, review, sales, price, ranking, ranking_weeks))
        
        connection.commit()

        time.sleep(2)
    
    cursor.close()