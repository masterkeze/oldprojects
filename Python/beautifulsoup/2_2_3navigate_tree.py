from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs0bj = BeautifulSoup(html.read(),"html.parser")
'''
for child in bs0bj.find("table",{"id":"giftList"}).children:
    print(child)

for decendant in bs0bj.find("table",{"id":"giftList"}).descendants:
    print(decendant)

for sibling in bs0bj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
'''
print(bs0bj.find("img",{"src":"../img/gifts/img1.jpg"
                        }).parent.previous_sibling.get_text())
