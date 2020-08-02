import win32api
import win32con
import time
import threading
def key():
    interval = 0.3
    while True:
        time.sleep(interval)
        win32api.keybd_event(65,0,0,0) #a键位码是86
        win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(83,0,0,0) #s键位码是86
        win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(68,0,0,0) #d键位码是86
        win32api.keybd_event(68,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(74,0,0,0) #j键位码是86
        win32api.keybd_event(74,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(75,0,0,0) #k键位码是86
        win32api.keybd_event(75,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(76,0,0,0) #l键位码是86
        win32api.keybd_event(76,0,win32con.KEYEVENTF_KEYUP,0)

def shua():
    time.sleep(5)
    win32api.keybd_event(70,0,0,0) #f键位码是70
    win32api.keybd_event(70,0,win32con.KEYEVENTF_KEYUP,0)
    print('press f')
    time.sleep(10)
    win32api.keybd_event(90,0,0,0) #z键位码是90
    win32api.keybd_event(90,0,win32con.KEYEVENTF_KEYUP,0)
    print('press z')
    time.sleep(25)
    win32api.keybd_event(70,0,0,0) #f键位码是70
    win32api.keybd_event(70,0,win32con.KEYEVENTF_KEYUP,0)
    print('press f')
    time.sleep(2)
    win32api.keybd_event(70,0,0,0) #f键位码是70
    win32api.keybd_event(70,0,win32con.KEYEVENTF_KEYUP,0)
    print('press f')
    time.sleep(2)
    win32api.keybd_event(70,0,0,0) #f键位码是70
    win32api.keybd_event(70,0,win32con.KEYEVENTF_KEYUP,0)
    print('press f')
    time.sleep(6)
    win32api.keybd_event(70,0,0,0) #f键位码是70
    win32api.keybd_event(70,0,win32con.KEYEVENTF_KEYUP,0)
    print('press f')

for t in range(5):
    shua()
    
