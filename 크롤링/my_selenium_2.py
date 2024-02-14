from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

url = "https://section.cafe.naver.com/ca-fe/home"


# req = requests.get(url)
# html = req.text
# print(html)

driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source
print(html)
# soup = BeautifulSoup(html, "html.parser")

# query = soup.select_one('#query')
# print(query)