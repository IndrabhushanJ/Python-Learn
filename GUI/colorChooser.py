from tkinter import *
from tkinter import colorchooser  # submodule


def click():
    color = colorchooser.askcolor()
    # print(color)
    colorHex = color[1]
    window.config(bg=colorHex)


window = Tk()
window.geometry('420x420')

button = Button(window, text='click me', command=click)
button.pack()



window.mainloop()
