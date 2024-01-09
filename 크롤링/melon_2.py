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

# lst50 = soup.select(".lst50")
# lst100 = soup.select(".lst100")
# lst_all = lst50 + lst100

rank = 1

# find_all 사용시
lst_all = soup.find_all(class_ = ["lst50", "lst100"])
# select 사용시
lst_all = soup.select(".lst50, .lst100")

singer_base_link = "https://www.melon.com/artist/timeline.htm?artistId="
album_base_link =  "https://www.melon.com/album/detail.htm?albumId="

def get_nums(song_num_text):
    # 리스트 컴플리헨션 사용하여
    # song_num = []
    # for num in song_num_text:
    #     if num.isdigit():
    #         song_num.append(num)
    song_num = "".join([num for num in song_num_text if num.isdigit()])
    return song_num

for i in lst_all:
    
    title = i.select_one(".ellipsis.rank01 a")

    singer = i.select_one(".ellipsis.rank02 a")
    singer_link = get_nums(singer["href"])

    album = i.select_one(".ellipsis.rank03 a")
    album_link = get_nums(album["href"])

    print("------------------------------")
    # print(f'[순위 : {rank1}]')
    
    print(f'{rank}위는 "{singer.text}"의 "{title.text}"입니다!!\n{album.text}의 수록곡 입니다!!')
    print(f'"{singer.text}" 정보 => "{singer_base_link + singer_link}"')
    print(f'"{album.text}" 정보 => "{album_base_link + album_link}"')

    # print(f'제목 : {title.text}')
    # print(f'가수 : {singer.text}')
    # print(f'앨범 : {album.text}')
    print("------------------------------")

    rank += 1