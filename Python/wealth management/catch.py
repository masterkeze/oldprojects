###This file is for abtaining data from website "http://bj.58.com/diannao/"
### -*- coding:utf-8 -*-
### file: re_html.py
###
##import tkinter #界面库
##import urllib #url解析库
##import re # 正则表达式库
##
###coding=utf-8
##from pyExcelerator import * # excel文件读写库         
##        
##class Window:
##        def __init__(self, root):
##                self.root = root                                                        # 创建组件
##                self.label = Tkinter.Label(root, text = '输入URL:')
##                self.label.place(x = 5, y = 15)
##                self.entryUrl = Tkinter.Entry(root,width = 30) 
##                self.entryUrl.place(x = 65, y = 15)
##                self.get = Tkinter.Button(root, 
##                                text = '获取数据', command = self.Get)
##                self.get.place(x = 280, y = 15)
##                self.edit = Tkinter.Text(root,width = 470,height = 600)
##                self.edit.place(y = 50)
##        def Get(self):
##                url = self.entryUrl.get()                                               # 获取URL
##                page = urllib.urlopen(url)                                              # 打开URL
##                data = page.read()                                                      # 读取URL内容
##
##                p_prices = re.compile(r"""(?<=<td width="60" class="price">)[^<]*(?=</td>)""")
##                p_products = re.compile("""(?<=" target="_blank" class="t">)[^<]*(?=</a>)""")
##                p_places = re.compile("""(?<=/diannao/' class='u'>)[^<]*(?=</a>)""")
##                p_times = re.compile("""(?<=<td class="pd" width="70">)[^<]*(?=</td>)""")
##
##                prices = p_prices.findall(data)
##                products = p_products.findall(data)
##                places = p_places.findall(data)                              
##                times =  p_times.findall(data)
##
##                self.edit.insert(Tkinter.END, len(prices))
##                self.edit.insert(Tkinter.END, '/n')
##                self.edit.insert(Tkinter.END, len(products))
##                self.edit.insert(Tkinter.END, '/n')
##                self.edit.insert(Tkinter.END, len(places))
##                self.edit.insert(Tkinter.END, '/n')
##                self.edit.insert(Tkinter.END, len(times))
##                self.edit.insert(Tkinter.END, '/n')
##                for i in range(1,len(places)):
##                        self.edit.insert(Tkinter.END, prices[i]+'   ')
##                        self.edit.insert(Tkinter.END, products[i]+'   ')
##                        self.edit.insert(Tkinter.END, places[i]+'   ')
##                        self.edit.insert(Tkinter.END, times[i]+'/n')                    
##                
##                page.close()
##root = Tkinter.Tk()
##window = Window(root)
##root.minsize(600,480)
##root.mainloop()


import urllib
from sgmllib import SGMLParser
 
class ListName(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.is_h4 = ""
		self.name = []
	def start_h4(self, attrs):
		self.is_h4 = 1
	def end_h4(self):
		self.is_h4 = ""
	def handle_data(self, text):
		if self.is_h4 == 1:
			self.name.append(text)
 
content = urllib.request.urlopen('http://list.taobao.com/browse/cat-0.htm').read()
listname = ListName()
listname.feed(content)
for item in listname.name:
	print (item.decode('gbk').encode('utf8'))
