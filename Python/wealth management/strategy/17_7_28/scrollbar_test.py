# this file is to test the scrollbar

from tkinter import *
global C,s
root = Tk()
root.title("scrollbar_test")
root.geometry('300x300+100+100')


def shownumber(x):

    C.delete(ALL)
    C.create_text(100,70,text = str(x),font=(font,15))

s = Scrollbar(root, orient = HORIZONTAL, jump = 0)
C = Canvas(root,bg='gray',xscrollcommand=s.set)

C.place(x=50,y=50,width=200,height=150)
s.place(x=50,y=200,width=200)

w = Scale(root, from_=0, to=1, orient = HORIZONTAL,showvalue = 0)
w["command"] = shownumber
w.place(x=50,y=250,width=200)

