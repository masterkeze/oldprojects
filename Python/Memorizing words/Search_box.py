#Search_UI
from tkinter import *
from urllib.request import urlopen
from bs4 import BeautifulSoup

def click_main():
    in_put = search_box_text.get()
    html = urlopen("http://dict.youdao.com/w/eng/%s/#keyfrom=dict2.index"\
                   %(in_put))
    bs0bj = BeautifulSoup(html,"html.parser")
    translation = bs0bj.find("li",{"class":""}).get_text()
    length = len(translation)
    if length > 25:
        n = length//25
        for i in range(1,n+3):
            translation = translation[:20*i+1]+'\n'+translation[20*i+1:]
    pronounce = bs0bj.findAll("span",{"class":"phonetic"})
    print(translation,pronounce)
    if pronounce != None:
        pronounce_eng = pronounce[0].get_text()
        pronounce_ame = pronounce[1].get_text()
    else:
        pronounce_eng = None
        pronounce_ame = None
    success = True
    if success:
        pop_translation(in_put,translation,pronounce_eng,pronounce_ame)
    print(in_put)
def pop_translation(in_put,translation,pronounce_eng,pronounce_ame):
    trans = Tk()
    trans.title(in_put)
    trans.geometry("400x400+470+100")
    title_label = Label(trans,text=in_put,font=(font,20),justify=LEFT)
    title_label.place(x=50,y=30,height=30)
    if pronounce_eng != None or pronounce_ame != None:
        pronounce_label = Label(trans,text="英[%s]; 美[%s]"%\
                                (pronounce_eng,pronounce_ame),font=('Phonetic',12))
        pronounce_label.place(x=50,y=80)
    trans_label = Label(trans,text="%s"%(translation),font=(font,12),justify=LEFT,anchor='w')
    trans_label.place(x=50,y=120,width=350)

    trans.mainloop()
root = Tk()
root.title("Search Box")
root.geometry("400x400+50+100")

title = Label(root,text="Keze Search",font=(font,24),justify=CENTER)
title.place(x=50,y=50,width=300,height=35)

search_box_text = StringVar()
search_box = Entry(root,textvariable=search_box_text,font=(font,17))
search_box.place(x=20,y=120,width=360,height=30)

search_button = Button(root,text='Search Now!',command = click_main)
search_button.place(x=150,y=200,width=100,height=40)

root.mainloop()

