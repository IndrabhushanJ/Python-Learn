from tkinter import *
from fileDialog import save, openfile


def cut():
    print("Text Cut.")


def copy():
    print("Text Copied.")


def paste():
    print("Text Pasted.")


window = Tk()

saveIcon = PhotoImage(file='icons8-save-16.png')
openIcon = PhotoImage(file='open_folder.png')
exitIcon = PhotoImage(file='exit.png')
cutIcon = PhotoImage(file='cut_Icon.png')
copyIcon = PhotoImage(file='copy_Icon.png')
pasteIcon = PhotoImage(file='paste_Icon.png')

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=('MV Boli', 15))
menubar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Open', command=openfile, image=openIcon, compound=LEFT)
fileMenu.add_command(label='Save', command=save, image=saveIcon, compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=quit, image=exitIcon, compound=LEFT)

editMenu = Menu(menubar, tearoff=0, font=('MV Boli', 15))
menubar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut', command=cut, image=cutIcon, compound=LEFT)
editMenu.add_command(label='Copy', command=copy, image=copyIcon, compound=LEFT)
editMenu.add_command(label='Paste', command=paste, image=pasteIcon, compound=LEFT)

window.mainloop()
