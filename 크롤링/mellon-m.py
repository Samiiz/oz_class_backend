from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import time

user_agent = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"

options = Options()
options.add_argument(f"user-agent={user_agent}")
options.add_experimental_option('detach', True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('excludeSwitches', ['enable-automation'])

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(1)

if driver.current_url != url:
    driver.get(url)

# a태그를 활용하여 웹페이지의 하이퍼링크를 식별한다.
driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(1)

driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click()
time.sleep(1)

# title ellipsis
# name ellipsis

melon_chart = driver.find_element(By.CSS_SELECTOR, "#_chartList")
list_100 = melon_chart.find_elements(By.CSS_SELECTOR, ".list_item")
time.sleep(1)


action = ActionChains(driver)

for i in list_100:
    title = i.find_element(By.CSS_SELECTOR, ".title.ellipsis")
    singer = i.find_element(By.CSS_SELECTOR, ".name.ellipsis")
    
    action.move_to_element(i).perform()
    i.find_element(By.CSS_SELECTOR, ".name.ellipsis").click()
    time.sleep(0.5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    driver.back()

    print()
    print(title.text)
    print(singer.text)
    time.sleep(0.5)