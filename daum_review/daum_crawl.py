import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#https://movie.v.daum.net/v/20180216105516049
#https://movie.v.daum.net/v/20160322133447390
#https://movie.v.daum.net/v/20160119102000376
#https://movie.v.daum.net/v/20140208130504016
#https://movie.v.daum.net/v/20130524150005739
#https://movie.v.daum.net/v/20130517080104720

driver = webdriver.Chrome('./driver/chromedriver.exe')
driver.set_window_size(1200, 800)
driver.implicitly_wait(3)
f = open('daum.txt', 'r')
lines = f.readlines()
i = 1
for line in lines:
    driver.get(line)
    contents = driver.find_element_by_xpath('//*[@id="mArticle"]').text
    if not contents:
        continue
    title = driver.find_element_by_xpath('//*[@id="cSub"]/div/h3').text
    year = driver.find_element_by_xpath('//*[@id="cSub"]/div/span/span[2]').text

    content = contents.split('칼럼니스트')[0]
    year = year.split('입력 ')[1]
    year = year[0:4]

    title = title.split('<')[1]
    title = title.split('>')[0]
    title = title.replace('\n', '').replace(':', ' ').replace('\\', '').replace('*', '').replace('?', '').replace('<',
                                                                                                                  '').replace(
        '>', '').replace('|', '').replace('/', '').replace('"', '')
    a = title + '(' + year + ').txt'
    f2 = open(a, 'a+', encoding='utf-8', newline='')
    f2.write(contents.replace('\n',''))
    print(a)
f.close()