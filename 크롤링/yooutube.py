import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

base_url = "https://www.youtube.com/results?search_query="
key_word = input("검색어를 입력하세요: ")

url = base_url + key_word
req = requests.get(url, headers=header)
html = req.text
soup = BeautifulSoup(html, "html.parser")

# 수정된 선택자를 사용하여 각 비디오에 대한 클래스 변경
videos = soup.select("#dismissible")

if videos:
    for video in videos:
        title = video.select_one("yt-formatted-string")
        name = video.select_one("a.yt-simple-endpoint.style-scope.yt-formatted-string")
        # date = video.select_one("")
        view = video.select_one("span.inline-metadata-item.style-scope.ytd-video-meta-block")
        
        print("------------------------------")
        print(f'제목: {title.text}')
        print(f'작성자: {name.text}')
        # print(f'게시날짜: {date.text}')
        print(f'조회수: {view.text}')
        print("------------------------------")
else:
    print("클래스 변경 필요")
