from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/oage1.html")
print(html.read())
