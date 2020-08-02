from tkinter import *

global root, C
global B3_holding, B3_x, B3_y, base_x, base_y

B3_holding = False
B3_x = -1
B3_y = -1
base_x = 0
base_y = 0

window_height = 600
window_width = 800
canvas_height = 9 / 10 * window_height
canvas_width = 3 / 4 * window_width

def draw(x, y):
    r = 10
    C.delete("all")
    if x >= 0 and y >= 0:
        if x <= window_width and y <= window_height:
            C.create_oval(x - r, y - r, x + r, y + r, outline="red", fill="red")
    return None


def paint(event):
    r = 3
    C.create_oval(event.x - r, event.y - r, event.x + r,
                  event.y + r, fill="red", outline="red")
    return None


def motion(event):
    print("Mouse position: (%s, %s)" % (event.x, event.y))
    return None


def click_b3(event):
    print("click")
    global B3_holding, B3_x, B3_y
    B3_holding = True
    B3_x = event.x
    B3_y = event.y
    print(base_x, base_y)
    return None


def hold_b3(event):
    if not B3_holding:
        return None
    global B3_x, B3_y, base_x, base_y
    diff_x = event.x - B3_x
    diff_y = event.y - B3_y
    base_x += diff_x
    base_y += diff_y
    B3_x = event.x
    B3_y = event.y
    if (diff_x ** 2 + diff_y ** 2) > 2:
        draw(base_x, base_y)
    # print(diff_x,diff_y)
    # print("Mouse position: (%s, %s)" % (event.x,event.y))
    print("Base position: (%s, %s)" % (base_x, base_y))
    return None


def release_b3(event):
    print("release")
    global B3_holding
    B3_holding = False
    return None


def leave(event):
    global B3_holding
    B3_holding = False
    return None


root = Tk()
root.title('Demo')
root.geometry('%sx%s' % (window_width + 60, window_height))
C = Canvas(root, bg='alice blue', height=canvas_height, width=canvas_width)

C.place(x=0, y=window_height - canvas_height)
C.bind('<Button-3>', click_b3)
C.bind('<B3-Motion>', hold_b3)
C.bind('<ButtonRelease-3>', release_b3)
C.bind('<Leave>',release_b3)

# <Button-1> = left click
# <Button-2> = middle click
# <Button-3> = right click
# <Button-4> = scroll up
# <Button-5> = scroll down
# root.bind('<Button-2>',motion)
# <Motion> when a mouse button is held down
# <B1-Motion> for specific keys
# root.bind('<B3-Motion>',motion)
# <ButtonRelease-1> for button release
# <Double-Button-1> double click
# <Triple-Button-1> triple click
# <Leave> The mouse pointer left the widget
# <Shift-Up> called when holding both shift and up
# <Configure> called when the window size is changed
# https://www.python-course.eu/tkinter_events_binds.php

root.mainloop()
