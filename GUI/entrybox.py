# entry widget = textbox that accepts a single line of user input

from tkinter import *


def submit():
    username = entry.get()
    print("Hello", username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


window = Tk()

entry = Entry(window,
              font=('Arial', 50),
              fg='#00ff00',
              bg='black',
              show='*')
# entry.insert(0,'Enter your username')
entry.pack(side=LEFT)

submitButton = Button(window, text='Submit', command=submit)
submitButton.pack(side=RIGHT)

deleteButton = Button(window, text='Delete', command=delete)
deleteButton.pack(side=RIGHT)

backspaceButton = Button(window, text='Backspace', command=backspace)
backspaceButton.pack(side=RIGHT)

window.mainloop()
