from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://music.youtube.com/explore'

driver = webdriver.Chrome()
driver.get(url=url)

answer = driver.page_source
driver.close()
driver.quit()

soup = BeautifulSoup(answer, 'lxml')
title_block = soup.find('ytmusic-carousel', class_='carousel')
print(title_block)