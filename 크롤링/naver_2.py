import requests
from bs4 import BeautifulSoup

header_user = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36

url = "https://naver.com"

# get 방식 : 서버에 리소스(자원)를 요청, 데이터를 수신하는 기능
req = requests.get(url, headers=header_user)
# print(req.request.headers)
print(dir(req))