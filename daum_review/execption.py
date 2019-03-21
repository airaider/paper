import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#
#
#
#https://movie.v.daum.net/v/20140208130504016
#https://movie.v.daum.net/v/20130524150005739
#https://movie.v.daum.net/v/20130517080104720

driver = webdriver.Chrome('./driver/chromedriver.exe')
driver.set_window_size(1200, 800)
driver.implicitly_wait(1)

driver.get('https://movie.v.daum.net/v/20130517080104720')
contents = driver.find_element_by_xpath('//*[@id="mArticle"]').text

content = contents.split('칼럼니스트')[0]

f2 = open('미나 문방구(2016).txt', 'a+', encoding='utf-8', newline='')
f2.write(contents.replace('\n', ''))
f2.close()
driver.quit()