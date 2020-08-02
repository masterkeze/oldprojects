from tkinter import * 
root = Tk()

 
def _bind_test(event):
    ''''''
    print(event.keysym)

root.bind("<KeyPress> ",_bind_test(root))
