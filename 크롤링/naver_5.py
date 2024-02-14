import requests
from bs4 import BeautifulSoup

# 사람인 척 하기위한 코드
header = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
key_word = input("검색어를 입력하세요 : ")

# 탐색을 원하는 url
url = base_url + key_word
# 원하는 사이트의 데이터 요청하기
req = requests.get(url, headers=header)
html = req.text
soup = BeautifulSoup(html, "html.parser")

total_area = soup.select(".view_wrap")

if total_area:
    areas = total_area
else:
    print("클래스 변경 필요")

rank_num = 1

for i in areas:
    ad = i.select_one(".link_ad")
    if ad:
        print("광고입니다")
        continue
    print(f'[{rank_num}]')
    title = i.select_one(".title_link._cross_trigger")
    name = i.select_one(".name")
    print("------------------------------")
    print(f'제목 : {title.text}') # [슈퍼스타 - 0, 흥민짱 - 1]
    print(f'작성자 : {name.text}')
    print(f'주소 : {title['href']}')
    print("------------------------------")

    rank_num += 1