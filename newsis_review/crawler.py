from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome('./driver/chromedriver.exe')
driver.set_window_size(1200, 800)
driver.implicitly_wait(3)


f = open('movie_titles(ver2)', 'r')
lines = f.readlines()
i = 1
for line in lines:
    line=line.replace('(','').replace(')','')
    line = 'https://www.youtube.com/results?search_query='+line+'+예고편'
    driver.get(line)
    contents = driver.find_element_by_xpath('//*[@id="video-title"]').click()
    if not contents:
        continue
    title = driver.find_element_by_xpath('//*[@id="article"]/div[1]/h1').text
    title = title.split('영화')[1]
    text1 = title
    text1 = text1.replace('\n', '').replace(':', ' ').replace('\\', '').replace('*', '').replace('?', '').replace('<', '').replace('>', '').replace('|', '').replace('/', '').replace('"', '')
    contents = contents.replace('\n', '')
    a = text1 + '.txt'
    print(str(i)+':'+a)
    f2 = open(a, 'w', encoding='utf-8', newline='')
    f2.write(contents)
    i = i+1
    f2.close()
f.close()