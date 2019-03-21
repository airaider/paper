'''
import requests
import csv
from bs4 import BeautifulSoup
for j in range (2, 3):#180
    line = 'https://brunch.co.kr/@hakus97/'+str(j)
    r = requests.get(line)
    c = r.content
    html = BeautifulSoup(c, "html.parser")
    i = 0
    title = html.find('h1', {'class': 'cover_title'})
    content = html.find('p', {'class': 'wrap_item item_type_text'})
    print(title.text)
    print(content)

'''

from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome('./driver/chromedriver.exe')
driver.set_window_size(1200, 800)
driver.implicitly_wait(3)

for j in range (2,180):
    line = 'https://brunch.co.kr/@hakus97/'+str(j)
    driver.get(line)
    contents = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]').text
    if not contents:
        continue
    title = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[3]/h1').text
    year = driver.find_element_by_xpath('//*[@id="wrapArticleInfo"]/span[4]').text

    if '<' not in title:
        continue
    title = title.split('<')[1]
    title = title.split('>')[0]
    year = year.split('.')[1]
    year = year[1:]
    text1 = title
    text1 = text1.replace('\n', '').replace(':', ' ').replace('\\', '').replace('*', '').replace('?', '').replace('<',
                                                                                                                  '').replace(
        '>', '').replace('|', '').replace('/', '').replace('"', '')
    contents = contents.replace('\n', '')

    a = text1 + '(' + year + ').txt'
    f2 = open(a, 'a+', encoding='utf-8', newline='')
    f2.write(contents)
    print(j+':'+a)
#f.close()