import requests
import csv
from bs4 import BeautifulSoup

r = requests.get('http://www.newsis.com/search/schlist/?val=%255B%25EC%2598%2581%25ED%2599%2594%2520%25EB%25A6%25AC%25EB%25B7%25B0%255D&sort=acc&jo=sub&bun=direct&sdate=&term=allday&edate=&s_yn=Y&catg=1&t=1&page=13&c[]=10600') #크롤링할 사이트 주소
c = r.content
i=0
html = BeautifulSoup(c, "html.parser")
div = html.find("strong",{"class" : "title"}) #all text
for link in html.find_all('a'):
    if '/view?id=NISX' in link.get('href') and i%2==0:
        print(link.get('href'))
    i=i+1
