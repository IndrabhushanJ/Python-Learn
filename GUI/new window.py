from tkinter import *


def createWindow():
    # newWindow = Toplevel()  # Toplevel() = new window 'on-top' of other windows, linked to 'bottom' window
    newWindow = Tk()  # Tk() = independent window
    oldWindow.destroy()


oldWindow = Tk()

Button(oldWindow, text='New Window', command=createWindow).pack()

oldWindow.mainloop()
