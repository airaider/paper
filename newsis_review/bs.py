from selenium import webdriver
from time import sleep
import requests
import csv
from bs4 import BeautifulSoup

f = open('newsis2.txt', 'r')
lines = f.readlines()
i = 1
for line in lines:
    line = 'http://www.newsis.com'+line
    r = requests.get(line)
    c = r.content
    html = BeautifulSoup(c, "html.parser")
    title = html.find('div', {'class': 'article_tbx mgt8 w970'})
    year = html.find('div', {'class': 'date'})
    contents = html.find('div', {'id': 'textBody'})
    title = title.text
    contents = contents.text
    contents.replace('\n', '')
    year=year.text

    year = year.split('등록 ')[1]
    year = year[0:4]

    title = title.split('영화')[1]
    title = title.replace('\'', '\\').replace('‘', '\\').replace('’','\\')
    title = title.split('\\')[1]

    title = title.split('\\')[0]
    title = title.replace('\n', '').replace(':', ' ').replace('\\', '').replace('*', '').replace('?', '').replace('<',
                                                                                                                  '').replace(
        '>', '').replace('|', '').replace('/', '').replace('"', '')
    a = title + '(' + year + ').txt'
    f2 = open(a, 'a+', encoding='utf-8', newline='')
    f2.write(contents.replace('\n',''))
    print(a)
f.close()