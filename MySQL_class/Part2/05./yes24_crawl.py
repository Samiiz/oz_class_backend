from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

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

# print(link_list)

# print(len(link_list))

# bookNum = 0
# for link in link_list:
#     if bookNum < 72:
#         browser.get(link[bookNum])
#         bookNum += 1
#     else:
#         break

browser.get(link_list[0])

title = browser.find_element(By.CLASS_NAME, 'gd_name').text
print(f'\n제목 : {title}')

author = browser.find_element(By.CLASS_NAME, 'gd_auth').text
print(f'저자 : {author}')

publisher = browser.find_element(By.CLASS_NAME, 'gd_pub').text
print(f'출판사 : {publisher}')

publishing = browser.find_element(By.CLASS_NAME, 'gd_date').text
print(f'출판일 : {publishing}')

rating = browser.find_element(By.CLASS_NAME, 'yes_b').text
print(f'평점 : {rating}점')

review = browser.find_element(By.CLASS_NAME, 'txC_blue').text
print(f'리뷰 : {review}개')

sales = browser.find_element(By.CLASS_NAME, 'gd_sellNum').text.split(' ')[2]
print(f'판매지수 : {sales}권')

price = browser.find_element(By.CLASS_NAME, 'nor_price').text
print(f'판매가 : {price}')

rangking = browser.find_element(By.CLASS_NAME, 'gd_best').text.split(' | ')[0]
if rangking :
    print(rangking)
else:
    print('랭킹 없음')

rangking_weeks = browser.find_element(By.CLASS_NAME, 'gd_best').text.split(' | ')[1]
if rangking_weeks :
    print(rangking_weeks)
else:
    print('주간랭킹 없음')
 으아아아아아
browser.quit()

# 책 제목
# title

# 저자
# author

# 출판사
# publisher

# 출판일
# publishing

# 평점
# rating

# 리뷰
# review

# 판매지수
# sales

# 가격
# price

# 국내도서랭킹
# rangking

# 국내도서 TOP100
# rangking_weeks