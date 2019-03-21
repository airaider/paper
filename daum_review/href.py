import requests
from bs4 import BeautifulSoup
f=open('daum.txt', 'w', encoding='utf-8', newline='')
w = 1
for j in range (1, 11):
    line = 'https://movie.daum.net/magazine/series?id=310&page='+str(j)
    r = requests.get(line)
    c = r.content
    html = BeautifulSoup(c, "html.parser")
    i = 0
    for link in html.find_all('a', href=True):
        if 'http://v.movie.daum.net' in link['href']:
            id=link['href']

            if i % 3 == 0:
                f.writelines(id)
                f.writelines("\n")
                print(w,':', id)
                w=w+1
            i=i+1
f.close()





