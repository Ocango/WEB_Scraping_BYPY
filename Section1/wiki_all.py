from urllib.request import urlopen
import re

from bs4 import BeautifulSoup

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html,'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id = 'mw-content-text').find_all('p')[0])
        print(bs.find(id = 'ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('页面有些元素不存在！')
    for link in bs.find_all('a',href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print('-'*20)
                print(newpage)
                pages.add(newpage)
                getLinks(newpage)

getLinks('')

#这个可以理解成递归的深度遍历