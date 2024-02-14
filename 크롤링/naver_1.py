import requests
from bs4 import BeautifulSoup

url = "https://naver.com"

# get 방식 : 서버에 리소스(자원)를 요청, 데이터를 수신하는 기능
req = requests.get(url)
html = req.text
#print(html)

soup = BeautifulSoup(html, "html.parser")
query = soup.select_one(".search_input")
print(query)