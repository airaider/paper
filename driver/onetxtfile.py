import requests
import csv
from bs4 import BeautifulSoup

f = open('new.txt', 'r')
lines = f.readlines()
f1 = open('review.IMDB.txt', 'w')
for line in lines:
    r = requests.get(line)
    c = r.content
    html = BeautifulSoup(c, "html.parser")
    res = html.find_all('div', 'text show-more__control')

    for n in res:
        print(n)
        print('1')
        print(n.get_text())


f.close()
f1.close()