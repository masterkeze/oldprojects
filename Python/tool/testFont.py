FONTS=['Arial', 'Courier New', 'Comic Sans MS', 'Fixedsys', 'MS Sans Serif', 'MS Serif', 'Symbol', 'System', 'Times New Roman', 'Verdana','Phonetic']

from tkinter import *
MAX_ROWS = 9
root = Tk()
root.title("Fonts")
row = 0
col = 0
for font in FONTS:
  e = Label(root, text=font, font=(font,12, 'bold','italic'))
  e.grid(row=row, column=col)
  row += 1
  e = Label(root, text=font, font=(font,13, 'italic'))
  e.grid(row=row, column=col)
  row += 1
  e = Label(root, text=font, font=(font, 14))
  e.grid(row=row, column=col)
  row += 1  
  if (row >= MAX_ROWS):
    row = 0
    col += 1
root.mainloop()
