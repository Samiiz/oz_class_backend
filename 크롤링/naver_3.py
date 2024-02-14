import requests
from bs4 import BeautifulSoup

# 사람인 척 하기위한 코드
header = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=thsgmdals&qdt=0&ie=utf8&query="
key_word = input("검색어를 입력하세요 : ")

# 탐색을 원하는 url
url = base_url + key_word
# 원하는 사이트의 데이터 요청하기
req = requests.get(url, headers=header)
html = req.text
soup = BeautifulSoup(html, "html.parser")

# print(soup)

# name : 작성자
# title_link _cross_trigger : 글의 제목

title = soup.select(".title_link._cross_trigger")
name = soup.select(".nmae")

for i in zip(title, name):
    print("------------------------------")
    print(f'제목 : {i[0].text}') # [슈퍼스타 - 0, 흥민짱 - 1]
    print(f'작성자 : {i[1].text}')
    print(f'주소 : {i[0]['href']}')
    print("------------------------------")