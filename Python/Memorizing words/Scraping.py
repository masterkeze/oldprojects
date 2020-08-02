from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://dict.youdao.com/w/eng/apple/#keyfrom=dict2.index")
bs0bj = BeautifulSoup(html,"html.parser")

##nameList = bs0bj.findAll("span",{"class":"def"})
translation = bs0bj.find("li",{"class":""}).get_text()
pronounce = bs0bj.findAll("span",{"class":"phonetic"})
pronounce_eng = pronounce[0].get_text()
pronounce_ame = pronounce[1].get_text()

##for name in nameList:
##    print(name.get_text())
