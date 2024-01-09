import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

#1~50위 lst50
#제목 .ellipsis.rank01 a
#가수 .ellipsis.rank02 a
#51~100위 lst100

lst50 = soup.select(".lst50")
lst100 = soup.select(".lst100")
lst_all = lst50 + lst100
rank = 1

for i in lst_all:
    print("------------------------------")
    # print(f'[순위 : {rank1}]')
    title = i.select_one(".ellipsis.rank01 a")
    singer = i.select_one(".ellipsis.rank02 a")
    album = i.select_one(".ellipsis.rank03 a")
    print(f'{rank}위는 "{singer.text}"의 "{title.text}"입니다!!\n{album.text}의 수록곡 입니다!!')
    # print(f'제목 : {title.text}')
    # print(f'가수 : {singer.text}')
    # print(f'앨범 : {album.text}')
    print("------------------------------")
    rank += 1