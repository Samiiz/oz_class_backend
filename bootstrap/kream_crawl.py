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

# for 문으로 돌려서 각각
# https://kream.co.kr/search // 전체 상품 주소
# https://kream.co.kr/search?gender={men, women, kidz} //성별 별 주소
# https://kream.co.kr/search?gender={men, women, kidz}&shop_category_id={각각 카테고리별 주소}
# 아우터 전체 62 / 자켓 22, 아노락 72, 코트 21, 패딩 20, 기타 아우터 72
# 신발 전체 34 / 스니커즈 1, 샌들/슬리퍼 37 , 플랫 70, 로퍼 69, 더비/레이스업 55, 부츠 35, 기타 신발 71
# 상의 전체 64 / 
# cssselector로 선택하는게 나을까... 아니면 각 카테고리별로 리스트를 만들어서 크롤링을 할까...... 흠....
# 멘토링 질문이다 이건!!
# 
# 
# 
# 
# 





# browser.find_element(By.CSS_SELECTOR, 

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
# 아 근데 중복되네................................
# 아니지, 전체상품 보여줄때만 중복제거 해서 보여주면 되잖아
# male, female, kidz 로 나뉘고 all_products 보여줄때는 중복 제거해서 보여주면 되겠다
# 그러면 pk 빼고 성별 / 카테고리 / 이너 카테고리 별로 긁어와서 okeu dokey


# for 성별
#   category_gender = 해당성별
#   for 상위 카테고리
#       category_products = 해당 카테고리
#       for 하위 카테고리
#           category_inner = 해당 하위 카테고리
#           객체 하나씩 들어가서
#           product_name, brand, model_number ,price_released ,price_last ,representative_color ,directly_buy ,directly_sell 추출
#           하고나서 spl = insert into ...
#           근데 이게 효율이 좋을까...
# 
# 




# products

# category_gender = for문에 따라서 male, female, kidz
# category_products = for문에 따라서 아우터 ~ 가구 리빙
# category_inner = category_products에 따라서 for문으로 진행
# product_name = .main-title-container > .title
# brand = .left-container > .title-text 안나오면 .subtitle
# model_number = .detail-box[2] > .product_info
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