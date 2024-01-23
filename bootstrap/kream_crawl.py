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




# 회원가입시 데이터베이스에 추가
# customers

# [PK]customer_ID
# customer_password
# customer_NAME
# contact
# [PK]email
# address




# 진행 과정
# for문은 두가지로 나눈다 1. 전체상품 / 2. 신규상품
# 
# 
# 
# 



# products

# category_gender = for문에 따라서 male, female, kidz
# category_products = for문에 따라서 아우터 ~ 가구 리빙
# category_inner = category_products에 따라서 for문으로 진행
# product_name = .main-title-container > .title
# brand = .left-container > .title-text 안나오면 .subtitle
# [PK]model_number = .detail-box[2] > .product_info
# price_released = detail-price > .price_info[1]
# price_last = .detail-box[1] > .product_info
# representative_color = .color-target
# directly_buy = btn_action [1] .pricr > .num
# directly_sell = btn_action [2] .pricr > .num


# 주문시 데이터베이스에 추가
# orders

# [PK]orderID
# [PK]customer_ID
# product_name
# orderDate
# [PK]model_number
# totalAmount


# 장바구니 추가시 데이터베이스에 추가
# cart

# customer_ID
# product_name
# model_number
# price_released
# price_last
# directly_buy