from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = "https://www.naver.com"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(4)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

query = soup.select_one('#query')
print(query)