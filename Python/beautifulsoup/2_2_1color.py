from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs0bj = BeautifulSoup(html,"html.parser")
'''
nameList = bs0bj.findAll("span",{"class":"green"})
for name in nameList:
    print(name.get_text())


headList = bs0bj.findAll({"h1","h2","h3","h4","h5","h6"})
for head in headList:
    print(head.get_text())

nameList = bs0bj.findAll(text="the prince")
print(len(nameList))
print(nameList)
'''
allText = bs0bj.findAll(id="text")
print(allText[0].get_text())
