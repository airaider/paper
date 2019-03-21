import requests
import csv
from bs4 import BeautifulSoup

f = open('new_title.txt', 'r')
lines = f.readlines()

for line in lines:
    r = requests.get(line)  # 크롤링할 사이트 주소
    c = r.content
    html = BeautifulSoup(c, "html.parser")
    res = html.find_all('div', 'parent')
    div = html.find("div", {"class": "parent"})
    res1 = html.find_all('div', 'text show-more__control')
    for i in res:
        text1 = str(div.text)
        text1 = text1.replace('\n', '')
        text1 = text1.replace(':', '')
        text1 = text1.replace('\\', '')
        text1 = text1.replace('*', '')
        text1 = text1.replace('?', '')
        text1 = text1.replace('<', '')
        text1 = text1.replace('>', '')
        text1 = text1.replace('|', '')
        text1 = text1.replace('<', '')
        text1 = text1.replace('/', '')
        text1 = text1.replace('"', '')
        text1 = text1.replace('              ', '')
        text1 = text1.replace('         ', '')
        text1 = text1+'.csv'
        f1 = open(text1, 'w', encoding='utf-8', newline='')
    wr = csv.writer(f1)
    for n in res1:
        for e in n.findAll('br'):
            e.replace_with(' ')
        wr.writerow([n.get_text()])
    f1.close()
f.close()

