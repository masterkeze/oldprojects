from urllib.request import urlopen
from bs4 import BeautifulSoup
import re#正则表达式

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs0bj = BeautifulSoup(html.read(),"html.parser")
images = bs0bj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])
