from urllib.request import urlopen
import re,datetime,random

from bs4 import BeautifulSoup

'''
https://en.wikipedia.org/wiki/Kevin_Bacon
'''

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen('https://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html,'html.parser')
    return bs.find('div',{'id':'bodyContent'}).find_all('a',href = re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')
while len(links) >0 :
    newArticle = links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)