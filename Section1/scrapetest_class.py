from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(),'html.parser')

namelist = bs.find_all('span',{'class':'green'})
for name in namelist:
    print(name.get_text())

