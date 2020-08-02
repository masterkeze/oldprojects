from tkinter import *
from tkinter import ttk

width = 600
height = 400
root = Tk()
root.title("Strategy Test")
root.geometry('%sx%s+100+50'%(width,height))

C = Canvas(root, bg='alice blue',height = height*3/4, width = width*3/4)
C.place(x=0,y=0)

code_num = StringVar()
entry_num = Entry(root,textvariable = code_num, width = int(width/55), borderwidth = 2)
code_num.set('000000')
entry_num.place(x=width*56/64,y=10)

code_al = StringVar()
titleChosen = ttk.Combobox(root,width = 5, state = 'readonly')
titleChosen['values'] = ('SH#','SZ#')
titleChosen.current(0)
titleChosen.place(x=width*49/64,y=10)



##root.mainloop()
