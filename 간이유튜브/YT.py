from selenium import webdriver
from bs4 import BeautifulSoup
import time

header = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

# 검색시 사용되는 주소와 검색어를 분리하여 input내용으로 검색되게 나눈다.
base_url = "https://www.youtube.com/results?search_query="
key_word = input("검색어를 임력하세요 : ")
# 나눈 두개의 변수를 합쳐서 input 내용으로 검색되게끔 url에 할당한다.
url = base_url + key_word

# driver 변수를 사용하여 webdriver.Chrome()이라는 브라우저 조작 함수를 이용할 수 있다
driver = webdriver.Chrome()
# 브라우저를 조작하여 url에서 정보를 get! 받아온다
driver.get(url)
time.sleep(5)

# for문을 이용하여 스크롤을 내린다
# 스크롤 안됨
for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)

# html 변수에 driver.get(url)로 받아온 정보중 page_source 페이지 정보를 할당한다.
html = driver.page_source
# 뷰티플수프를 이용하여 html변수값을 parser (Dom형식으로 전환)한다. 
soup = BeautifulSoup(html, "html.parser")

videos = soup.select(".text-wrapper")

rank = 1

if videos:
    for video in videos:
        title = video.select_one("a.style-scope.ytd-video-renderer")
        name = video.select_one(".yt-simple-endpoint.style-scope.yt-formatted-string")
        metadata_container = video.select_one("#metadata")  # metadata 컨테이너 선택
        date = metadata_container.select_one("#metadata-line > span:nth-child(4)")
        view = metadata_container.select_one("#metadata-line > span")
        
        print(f'-----{rank}번----------------------')
        print(f'제목 : {"".join(title.text.split())}')
        print(f'작성자 : {"".join(name.text.split())}')
        print(f'게시날짜 : {date.text if date else "라이브 방송중"}')
        print(f'{view.text}')
        print("------------------------------")

        rank += 1
else:
    print("클래스 변경 필요")