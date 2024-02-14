import requests
from bs4 import BeautifulSoup

# 사람인 척 하기위한 코드
header = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
# 탐색을 원하는 url
url = "https://www.naver.com"
# 원하는 사이트의 데이터 요청하기
req = requests.get(url, headers=header)