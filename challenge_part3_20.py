import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = 'html.parser'
        sp = BeautifulSoup(html, parser)
        
        f = open('webscrape.txt', 'w')

        #print(sp.find_all('a'))
        
        
        for tag in sp.find_all('a'):
            #print(tag.get('href'))
            url = tag.get('href') #属性(url)の取得
            if url is None:
                print('OUT')
                continue
            if 'html' in url:
                print('\n' + url)
                f.writelines(url + '\n')

        f.close()


news = 'https://news.yahoo.co.jp/'
Scraper(news).scrape()


